# Generated by Django 4.0.2 on 2022-05-03 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venuehome', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeminarHall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Event_name', models.CharField(max_length=200, verbose_name='Event Name')),
                ('Department', models.CharField(max_length=200)),
                ('Date', models.DateField(verbose_name='Event Date')),
                ('Start_time', models.TimeField(verbose_name='Start time')),
                ('End_time', models.TimeField(verbose_name='End time')),
                ('Projector', models.CharField(max_length=20)),
            ],
        ),
    ]