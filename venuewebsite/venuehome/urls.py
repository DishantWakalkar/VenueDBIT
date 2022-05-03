from django.contrib import admin
from django.urls import path, include
from venuehome import views

urlpatterns = [ 
    path('', views.index, name="venuehome"),
    path('login', views.loginUser, name="login"),
    path('logout', views.logoutUser, name="logout"),

]