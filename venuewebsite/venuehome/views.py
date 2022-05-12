from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.views.generic import ListView, FormView
from matplotlib.style import available
from .models import Booking, Venue
from .forms import AvailablityForm
from .booking_functions.availabilty import check_availability

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render (request, 'index.html')

def loginUser(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate (request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect("/")

        else:
        # Return an 'invalid login' error message.
            return render (request, 'login.html')  

    return render (request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect ("/login")

def signupUser(request):
    if request.method == 'POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save();
        else:
            messages.info(request,'Password not matching')
            return redirect('signup')
        return redirect('/')
    
    else:    
        return render (request, 'signup.html')

def viewdetails(request):
    return render (request, 'Viewdetails.html')

def bookingform(request):
    return render (request, 'bookingform.html')
class VenueList(ListView):
    model=Venue

class BookingList(ListView):
    model=Booking

class BookingView(FormView):
    form_class= AvailablityForm
    template_name = 'availability_form.html'

    def form_valid(self, form):
        data = form.cleaned_data
        venue_list = Venue.objects.filter(category=data['venue_name'])
        available_venue=[]
        for venue in venue_list:
            if check_availability(venue, data['check_in'], data['check_out']):
                available_venue.append(venue)
