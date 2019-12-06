from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from .models import RegisterStudent
# Create your views here.



class IndexStudentView(TemplateView):
    template_name ='Student/index.html'
class RegisterstudentView(CreateView):
    model = RegisterStudent
    fields = ['first_name','last_name','dob','address','standard']