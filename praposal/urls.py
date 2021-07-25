from django.urls import path
from .views import *

app_name = "proposals"
urlpatterns = [
    path('proposals', ProposalView.as_view(), name='proposals'),
    path('proposal-single/<int:pk>', SingleProposalView.as_view(), name="single_proposal"),
    path('proposal-delete/<int:pk>', DeleteProposalView.as_view(), name="delete_proposal"),
    path('proposal-club', ProposalClubView.as_view(), name="club_proposal"),

]
