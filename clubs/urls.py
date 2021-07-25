from django.urls import path
from .views import *

app_name = "clubs"
urlpatterns = [
    path('clubs', ClubsView.as_view(), name='clubs'),
    path('club-update/<int:pk>', UpdateClubView.as_view(), name="update_club"),
    path('club-single/<int:pk>', SingleClubView.as_view(), name="single_club"),
]
