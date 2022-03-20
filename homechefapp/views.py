from django.shortcuts import render
from django.http import HttpResponse
import requests

# https://api.spoonacular.com/recipes/complexSearch?query=pasta&maxFat=25&number=2&apiKey=af8f73de917040b2b3b4e5b78fe4947a

# Create your views here.
# render method(1st param = request obj, 2nd param = template name (template path), 3rd param = {'key':'value'})
API_KEY_SPOONACULAR = 'af8f73de917040b2b3b4e5b78fe4947a'
 

def profile(request):
    return render(request, 'homechefapp/profile.html', {'webPageTitle': 'Profile', 'name':'Harry Potter'})

def login(request):
    return render(request, 'homechefapp/login.html', {'webPageTitle': 'Login'})

def register(request):
    return render(request, 'homechefapp/register.html', {'webPageTitle': 'Register'})

def about(request):
    return render(request, 'homechefapp/about.html', {'webPageTitle': 'About'})

def home(request):
    url = f'https://api.spoonacular.com/recipes/random?number=4&apiKey={API_KEY_SPOONACULAR}'
    response = requests.get(url)
    data = response.json()

    homeRecipes = data['recipes']

    context = {
        'recipes' : homeRecipes,
        'webPageTitle' : 'Home'
    }
    return render(request, 'homechefapp/home.html', context)