from django.urls import path , include
from . import views
from .views import EventListView, EventCreateView, EventUpdateView, EventDeleteView


urlpatterns = [
   
    path('events/', views.EventListView.as_view(), name='event-list'),
    path('create/', views.EventCreateView.as_view(), name='event-create'),
    path('edit/<int:pk>/', views.EventUpdateView.as_view(), name='event-edit'),
    path('delete/<int:pk>/', views.EventDeleteView.as_view(), name='event-delete'),
    path('events/', EventListView.as_view(), name='event-list'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
   
]