from django import forms
from .models import *


class ApplyMemberForm(forms.ModelForm):
    class Meta:
        model = ClubProfile
        fields = []


class UpdateClubForm(forms.ModelForm):
    moto = QuillField

    class Meta:
        model = ClubProfile
        fields = ['club_name', 'logo', 'moto', 'social_insta', 'social_face', 'social_twitter', 'club_banner']
        widget = {
                  'logo': forms.ImageField(), 'club_banner': forms.ImageField()
                  }
