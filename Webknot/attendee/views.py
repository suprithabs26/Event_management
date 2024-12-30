from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Attendee
from .forms import AttendeeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class AttendeeListView(LoginRequiredMixin, ListView):
    model = Attendee
    template_name = 'attendee/attendee_list.html'
    context_object_name = 'attendees'
    login_url = '/accounts/google/login/'

class AttendeeCreateView(CreateView):
    model = Attendee
    form_class = AttendeeForm
    template_name = 'attendee/attendee_form.html'
    success_url = reverse_lazy('attendee-list')

class AttendeeUpdateView(UpdateView):
    model = Attendee
    form_class = AttendeeForm
    template_name = 'attendee/attendee_form.html'
    success_url = reverse_lazy('attendee-list')

class AttendeeDeleteView(DeleteView):
    model = Attendee
    template_name = 'attendee/attendee_confirm_delete.html'
    success_url = reverse_lazy('attendee-list')