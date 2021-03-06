# Generated by Django 4.0.4 on 2022-05-10 13:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('venuehome', '0005_remove_seminarhall_end_time_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(choices=[('SH', 'SeminarHall'), ('MH', 'MondiniHall'), ('BH', 'BoscoHall'), ('FG', 'FootballGround'), ('BC', 'BasketballCourt'), ('UC', 'UpperCourt')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Event_Name', models.CharField(max_length=200, verbose_name='Event Name')),
                ('Department', models.CharField(max_length=200)),
                ('check_in', models.DateTimeField()),
                ('check_out', models.DateTimeField()),
                ('Estimated_people', models.CharField(max_length=200, verbose_name='Estimated people')),
                ('No_of_Chairs', models.CharField(max_length=200, verbose_name='Chairs required')),
                ('Projector', models.BooleanField()),
                ('Any_requirements', models.TextField(blank=True, verbose_name='Specify Requirements if any')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venuehome.venue')),
            ],
        ),
    ]
