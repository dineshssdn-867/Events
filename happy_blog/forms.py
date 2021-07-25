from django import forms
from .models import *


class HappyBlogForm(forms.ModelForm):
    tweet = QuillField
    class Meta:
        model = happy_blog
        fields = ['name', 'job_type', 'tweet', 'image']
        widget = {
                  'image': forms.ImageField(), 
                  }
