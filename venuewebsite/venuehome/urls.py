from django.contrib import admin
from django.urls import path, include
from venuehome import views
from .views import RoomList, BookingList

urlpatterns = [ 
    path('', views.index, name="venuehome"),
    path('login', views.loginUser, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path('signup', views.signupUser, name="signup"),
    path('viewdetails', views.viewdetails, name="viewdetails"),
    path('roomlist/', RoomList.as_view(), name="RoomList"),
    path('bookinglist/', BookingList.as_view(), name="BookingList"), 
]