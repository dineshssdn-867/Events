from django.urls import path
from .views import *

app_name = "contact"
urlpatterns = [
    path('', ContactUs.as_view(), name="contact"),
    path('submit', submit_query, name="submit_query")
]
