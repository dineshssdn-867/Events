from django.urls import path
from .views import *

app_name = "social_home"
urlpatterns = [
    path('', HomeView.as_view(), name="home"),
]
