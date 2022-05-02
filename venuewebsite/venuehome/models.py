from django.db import models

# Create your models here.
class Signin(models.Model):
   First_name = models.CharField('First Name',max_length=50)
   Last_name = models.CharField('Last Name',max_length=50)
   Email_id = models.EmailField('Email id',max_length=150)
   Phone_no = models.CharField('Phone number',max_length=50)
   Password = models.CharField('Password',max_length=50)

