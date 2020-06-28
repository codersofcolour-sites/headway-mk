from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView

from wagtail_events.models import Event


class EventDetailView(DetailView):
    model = Event