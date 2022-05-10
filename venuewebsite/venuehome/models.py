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

class SeminarHall(models.Model):
      Event_name = models.CharField('Event Name',max_length=200)
      Department = models.CharField(max_length=200)
      Date = models.DateField('Event Date')
      Projector = models.CharField(max_length=20)

      def __str__(self):
            return f'{self.Date} for {self.Event_name} '

class Mondini_Hall(models.Model):
      Event = models.CharField('Event ',max_length=200)
      Department = models.CharField(max_length=200)
      Date = models.DateField('Event Date')
      Start_time = models.TimeField('Start time')
      Estimated_people = models.CharField('No of people attending ',max_length=200)
      no_of_chairs = models.CharField('No of chairs required ',max_length=200)
      Projector = models.CharField(max_length=20)
      Any_requirements = models.TextField('Specify Requirements if any',blank=True)

class BoscoHall(models.Model):
      EventName = models.CharField('event',max_length=200)
      Department = models.CharField(max_length=200)
      Date = models.DateField('Event Date')
      Start_time = models.TimeField('Start time')
      End_time = models.TimeField('End time')

class Ground(models.Model):
     event = models.CharField('Occasion',max_length=200)
     Department = models.CharField(max_length=200)
     Date = models.DateField('Event Date')
     Start_time = models.TimeField('Start time')
     End_time = models.TimeField('End time')

class SeminarBooking(models.Model):
      user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
      hall = models.ForeignKey(SeminarHall, on_delete=models.CASCADE)
      Start_time = models.DateTimeField('Start time')
      End_time = models.DateTimeField('End time')

      def __str__(self):
            return f'{self.user} has booked {self.hall} from {self.Start_time} to {self.End_time}'

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
      Projector = models.BooleanField()
      Any_requirements = models.TextField('Specify Requirements if any',blank=True)

      def __str__(self):
            return f'{self.Event_Name}'