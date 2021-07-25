from django import forms
from .models import *


class CreateEvent(forms.ModelForm):
    description = QuillField
    proposal = QuillField
    class Meta:
        model = Event
        fields = ['event_title', 'time', 'date', 'event_poster', 'event_banner', 'description', 'proposal']


class ApplyEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = []


class UpdateEventForm(forms.ModelForm):
    description = QuillField
    proposal = QuillField
    class Meta:
        model = Event
        fields = ['event_title', 'time', 'date', 'event_poster', 'event_banner', 'description', 'proposal']
        widget = {
                  'event_poster': forms.ImageField(), 'event_banner':  forms.ImageField()
                  }



