from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# render method(1st param = request obj, 2nd param = template name (template path), 3rd param = {'key':'value'})

def profile(request):
    return render(request, 'homechefapp/profile.html', {'title': 'Profile', 'name':'Harry Potter'})

def login(request):
    return render(request, 'homechefapp/login.html', {'title': 'Login'})

def register(request):
    return render(request, 'homechefapp/register.html', {'title': 'Register'})

def about(request):
    return render(request, 'homechefapp/about.html', {'title': 'About'})

def home(request):
    return render(request, 'homechefapp/home.html', {'title': 'Home'})