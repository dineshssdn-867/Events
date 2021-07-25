from django import forms
from events.models import Event


class AcceptEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = []


