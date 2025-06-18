from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.userSignup.as_view()),
    path("getMembershipDetails/<email>/",views.userMembership.as_view()),
    path("createevent/", views.createEvent.as_view()),
    path("getEvent/",views.getEventDetails.as_view())
]
