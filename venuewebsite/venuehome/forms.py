from tabnanny import check
from django import forms

class AvailablityForm(forms.Form):
    VENUE_NAMES = (
            ('SH', 'SeminarHall'),
            ('MH', 'MondiniHall'),
            ('BH', 'BoscoHall'),
            ('FG', 'FootballGround'),
            ('BC', 'BasketballCourt'),
            ('UC', 'UpperCourt'),
      )
    venue_name = forms.ChoiceField(choices=VENUE_NAMES, required=True)
    check_in = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M", ])
    check_out = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M", ])
