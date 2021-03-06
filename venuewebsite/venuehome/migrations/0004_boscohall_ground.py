# Generated by Django 4.0.4 on 2022-05-03 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venuehome', '0003_mondini_hall'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoscoHall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EventName', models.CharField(max_length=200, verbose_name='event')),
                ('Department', models.CharField(max_length=200)),
                ('Date', models.DateField(verbose_name='Event Date')),
                ('Start_time', models.TimeField(verbose_name='Start time')),
                ('End_time', models.TimeField(verbose_name='End time')),
            ],
        ),
        migrations.CreateModel(
            name='Ground',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(max_length=200, verbose_name='Occasion')),
                ('Department', models.CharField(max_length=200)),
                ('Date', models.DateField(verbose_name='Event Date')),
                ('Start_time', models.TimeField(verbose_name='Start time')),
                ('End_time', models.TimeField(verbose_name='End time')),
            ],
        ),
    ]
