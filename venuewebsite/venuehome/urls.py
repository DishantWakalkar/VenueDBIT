from django.contrib import admin
from django.urls import path, include
from venuehome import views
from .views import BookingView, VenueList, BookingList

urlpatterns = [ 
    path('', views.index, name="venuehome"),
    path('login', views.loginUser, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path('signup', views.signupUser, name="signup"),
    path('availability_form', views.availability_form, name="availability_form"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('roomlist/', VenueList.as_view(), name="VenueList"),
    path('bookinglist/', BookingList.as_view(), name="BookingList"),
    path('bookingform', views.bookingform, name="bookingform"),
     path('book/', BookingView.as_view(), name="BookingView"),  
]
