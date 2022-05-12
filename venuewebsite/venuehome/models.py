from random import choices
from tokenize import Name
from django.db import models
from django.conf import settings
from django.forms import CharField

# Create your models here.
class Signin(models.Model):
      First_name = models.CharField('First Name',max_length=50)
      Last_name = models.CharField('Last Name',max_length=50)
      Email_id = models.EmailField('Email id',max_length=150)
      Phone_no = models.CharField('Phone number',max_length=50)
      Password = models.CharField('Password',max_length=50)

class Venue(models.Model):
      VENUE_NAMES = (
            ('SH', 'SeminarHall'),
            ('MH', 'MondiniHall'),
            ('BH', 'BoscoHall'),
            ('FG', 'FootballGround'),
            ('BC', 'BasketballCourt'),
            ('UC', 'UpperCourt'),
      )
      place = models.CharField(max_length=2, choices=VENUE_NAMES)

      def __str__(self):
            return f'{self.place}'

class Booking(models.Model):
      user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
      venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
      Event_Name= models.CharField('Event Name',max_length=200)
      Department = models.CharField(max_length=200)
      check_in = models.DateTimeField()
      check_out = models.DateTimeField()
      Estimated_people = models.CharField('Estimated people',max_length=200)
      No_of_Chairs = models.CharField('Chairs required',max_length=200)
      Projector = models.CharField('Projector required',max_length=1)
      Any_requirements = models.TextField('Specify Requirements if any',blank=True)

      def __str__(self):
            return f'{self.Event_Name}'