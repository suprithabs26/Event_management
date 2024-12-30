from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Event
from django.urls import reverse_lazy
from .serializers import EventSerializer
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from .forms import EventForm
from django.contrib.auth import logout
from .models import Profile
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin

def homepage(request):
    return render(request, 'events/home.html') 

def logout_view(request):
    logout(request)
    return redirect("/")

@login_required
def profile_view(request):
    return render(request, 'events/profile.html')



class EventViewSet(viewsets.ViewSet):
    
    def list(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            event = Event.objects.get(pk=pk)
            serializer = EventSerializer(event)
            return Response(serializer.data)
        except Event.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        try:
            event = Event.objects.get(pk=pk)
            serializer = EventSerializer(event, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Event.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            event = Event.objects.get(pk=pk)
            event.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Event.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    



class EventListView(LoginRequiredMixin, ListView):
    model = Event
    template_name = 'events/event_list.html'
    context_object_name = 'events'
    login_url = '/accounts/google/login/'


class EventCreateView(CreateView):
    model = Event
   # form_class = EventForm
    template_name = 'events/event_form.html'
    fields = ['name', 'description', 'location', 'date']
    success_url = reverse_lazy('event-list')

class EventUpdateView(UpdateView):
    model = Event
    #form_class = EventForm
    template_name = 'events/event_form.html'
    fields = ['name', 'description', 'location', 'date']
    success_url = reverse_lazy('event-list')

class EventDeleteView(DeleteView):
    model = Event
    template_name = 'events/event_confirm_delete.html'
    success_url = reverse_lazy('event-list')

