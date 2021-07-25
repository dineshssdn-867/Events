from django.urls import path
from .views import *

app_name = "events"
urlpatterns = [
    path('events', UpcomingEventView.as_view(), name='upcoming_events'),
    path('event-add/', CreateEventView.as_view(), name="create_event"),
    path('event-update/<int:pk>', UpdateEventView.as_view(), name="update_event"),
    path('event-single/<int:pk>', SingleEventView.as_view(), name="single_event"),
    path('event-delete/<int:pk>', DeleteEventView.as_view(), name="delete_event"),
    path('events-past', PastEventView.as_view(), name="past_event"),
    path('events-today', TodayEventView.as_view(), name="today_event"),
    path('events-club', ClubsEventView.as_view(), name="club_event"),
    path('events-rating/<int:pk>', CreateRatingView, name="rating_event"),
    path('events-calender/', CalenderEventView.as_view(), name="calender_event")
]
