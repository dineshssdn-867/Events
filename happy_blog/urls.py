from django.urls import path
from .views import *

app_name = "happy_blog"
urlpatterns = [
    path('happy-blog-add', HappyBlogView.as_view(), name='happy_blog_add'),
]
