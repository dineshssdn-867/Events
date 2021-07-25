from django.urls import path
from .views import *

app_name = "aboutus"
urlpatterns = [
    path('', AboutusView.as_view(), name="aboutus"),
]
