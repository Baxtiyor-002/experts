from django.shortcuts import render
from django.views.generic import ListView
from .models import Experts
# Create your views here.


class ExpertListView(ListView):
    model = Experts
    template_name = 'home.html'
