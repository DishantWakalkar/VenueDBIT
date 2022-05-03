from email.policy import HTTP
from http.client import HTTPResponse
from smtplib import SMTPResponseException
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from .models import SeminarHall



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

<<<<<<< Updated upstream
=======

    
>>>>>>> Stashed changes
