from django import forms
from .models import *


class CreateBlog(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ['blog_title', 'blog_poster', 'blog_banner', 'description']


class LikeForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = []


class UpdateBlogForm(forms.ModelForm):
    description = QuillField()

    class Meta:
        model = Blog
        fields = ['blog_title', 'blog_poster', 'blog_banner', 'description']
        widget = {
                  'blog_poster': forms.ImageField(), 'blog_banner':  forms.ImageField()
                  }