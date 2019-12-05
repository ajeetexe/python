from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request,'about.html')
def signIn(request):
    return render(request,'login.html')
def signUp(request):
    return render(request,'signup.html')