from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class TeacherView(TemplateView):
    template_name='Teacher/index.html'