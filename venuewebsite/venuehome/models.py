from django.db import models

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
   Start_time = models.TimeField('Start time')
   End_time = models.TimeField('End time')
   Projector = models.CharField(max_length=20)

class Mondini_Hall(models.Model):
   Event = models.CharField('Event ',max_length=200)
   Department = models.CharField(max_length=200)
   Date = models.DateField('Event Date')
   Start_time = models.TimeField('Start time')
   End_time = models.TimeField('End time')
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

class BasketBall_Court(models.Model):
     event = models.CharField('Occasion',max_length=200)
     Department = models.CharField(max_length=200)
     Date = models.DateField('Event Date')
     Start_time = models.TimeField('Start time')
     End_time = models.TimeField('End time')
