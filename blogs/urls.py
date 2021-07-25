from django.urls import path
from .views import *

app_name = "blogs"

urlpatterns = [
    path('blogs', HomeView.as_view(), name='blogs'),
    path('blog-add/', CreateBlogView.as_view(), name="create_blog"),
    path('blog-update/<int:pk>', UpdateBlogView.as_view(), name="update_blog"),
    path('blog-single/<int:pk>', SingleBlogView.as_view(), name="single_blog"),
    path('blog-delete/<int:pk>', DeleteBlogView.as_view(), name="delete_blog"),
]
