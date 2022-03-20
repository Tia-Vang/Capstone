from django.shortcuts import render
from django.http import HttpResponse
import requests

# https://api.spoonacular.com/recipes/complexSearch?query=pasta&maxFat=25&number=2&apiKey=af8f73de917040b2b3b4e5b78fe4947a

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
    #response = requests.get('')
    return render(request, 'homechefapp/home.html', {'title': 'Home'})

#todo: add a search results page, for you page
