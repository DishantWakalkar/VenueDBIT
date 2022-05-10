import datetime
from venuehome.models import SeminarHall, SeminarBooking 

def check_availability(hall, Start_time, End_time):
    avail_list[]
    booking_list = SeminarBooking.objects.filter(hall=hall)
    for booking in booking_list:
        if booking.Start_time > End_time or booking.End_time < Start_time:
            avail_list.append(True)
        else:
            avail_list.append(False)
    return all(avail_list)