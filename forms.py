# sports_event_management/main/forms.py
from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'date', 'location', 'description'] 
        widgets = {
               'date': forms.DateInput(attrs={'type': 'date'}),  # HTML5 date input
               'time': forms.TimeInput(attrs={'type': 'time'}),  # HTML5 time input
           }