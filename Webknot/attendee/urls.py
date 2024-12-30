# filepath: /C:/Users/abhis/Desktop/Assignment webknot/assignment/attendee/urls.py
from django.urls import path
from .views import AttendeeListView, AttendeeCreateView, AttendeeUpdateView, AttendeeDeleteView

urlpatterns = [
    path('', AttendeeListView.as_view(), name='attendee-list'),
    path('create/', AttendeeCreateView.as_view(), name='attendee-create'),
    path('update/<int:pk>/', AttendeeUpdateView.as_view(), name='attendee-update'),
    path('delete/<int:pk>/', AttendeeDeleteView.as_view(), name='attendee-delete'),
]