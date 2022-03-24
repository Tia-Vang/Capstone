from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.template import RequestContext
import requests
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterFrom

# Using Spoonacular API for homepage (note from Tia)
# https://api.spoonacular.com/recipes/complexSearch?query=pasta&maxFat=25&number=2&apiKey=af8f73de917040b2b3b4e5b78fe4947a
API_KEY_SPOONACULAR = 'af8f73de917040b2b3b4e5b78fe4947a'


# Create your views here.
# render method(1st param = request obj, 2nd param = template name (template path), 3rd param = {'key':'value'})


def profile(request):
    return render(request, 'homechefapp/profile.html', {'webPageTitle': 'Profile', 'name':'Harry Potter'})

#def login(request):
#    return render(request, 'homechefapp/login.html', {'webPageTitle': 'Login'})

def register(request):

    if request.method == 'POST':
        form = UserRegisterFrom(request.POST)
        if form.is_valid():
            form.save()
            #username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! Please login!')
            return redirect('login')
    else:
        form = UserRegisterFrom()
    return render(request, 'homechefapp/register.html', {'form':form , 'webPageTitle':'Register'})


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

def search(request):
    #TODO: change pasta to whatever is in the searchbar
    url = f'https://api.spoonacular.com/recipes/complexSearch?query=pasta&number=4&apiKey={API_KEY_SPOONACULAR}'
    response = requests.get(url)
    data = response.json()

    homeRecipes = data['results']

    context = {
        'recipes' : homeRecipes,
        'webPageTitle' : 'Results'
    }
    return render(request, 'homechefapp/results.html', context)

def for_you(request):
    # change 'vegitarian' to a list (using commas) of profile prefs
    query = request.GET.get('query')
    urlSearch = f'https://api.spoonacular.com/recipes/complexSearch?query={query}&number=4&apiKey={API_KEY_SPOONACULAR}'
    response = requests.get(urlSearch)
    data = response.json()
    
    searchRecipes = data['results']

    context = {
        'results' : searchRecipes,
        'webPageTitle' : 'For You'
    }


    #onlyveg = models.BooleanFields()

    return render(request, 'homechefapp/for_you.html', context)

#todo: add a search results page, for you page