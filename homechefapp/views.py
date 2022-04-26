from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.template import RequestContext
import requests
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterFrom, UserUpdateForm, ProfileUpdateForm

# Using Spoonacular API for homepage (150 quota/day)
# https://api.spoonacular.com/recipes/complexSearch?query=pasta&maxFat=25&number=2&apiKey=af8f73de917040b2b3b4e5b78fe4947a
API_KEY_SPOONACULAR = 'af8f73de917040b2b3b4e5b78fe4947a'

randomUrl = f'https://api.spoonacular.com/recipes/random?number=4&apiKey={API_KEY_SPOONACULAR}'


# Create your views here.
# render method(1st param = request obj, 2nd param = template name (template path), 3rd param = {'key':'value'})


#####################################_____REGISTER VIEW______#####################################
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


#####################################_____PROFILE VIEW______#####################################
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your profile has been updated.')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'webPageTitle': 'Profile'

    }
    return render(request, 'homechefapp/profile.html', context)


#####################################_____RESULTS VIEW______#####################################
def results(request):

    if request.method == 'POST':
        ingredients = request.POST['ingredients']
        ingredientUrl = f'https://api.spoonacular.com/recipes/complexSearch?includeIngredients={ingredients}&number=100&apiKey={API_KEY_SPOONACULAR}'
         
        response = requests.get(ingredientUrl)
        data = response.json()
        recipes = data['results']

        context = {
            'data': data,
          'recipes' : recipes,
           'webPageTitle' : 'Results'
        }

        return render(request, 'homechefapp/results.html', context)


#####################################_____RECIPE VIEW______#####################################
def recipe(request, id):
    recipeUrl = f'https://api.spoonacular.com/recipes/{id}/information?includeNutrition=false&apiKey={API_KEY_SPOONACULAR}'
    response = requests.get(recipeUrl)

    data = response.json()

    ing = data['extendedIngredients']
    inst = data['analyzedInstructions']


    context = {
            'data': data,
            'ing': ing,
            'inst': inst,
           'webPageTitle' : 'Recipe'
    }

    return render(request, 'homechefapp/recipe.html', context)



#####################################_____FORYOU VIEW______#####################################
def for_you(request):
    response = requests.get(randomUrl)
    data = response.json()
    homeRecipes = data['recipes']

    context = {
          'recipes' : homeRecipes,
           'webPageTitle' : 'Home',
    }

    return render(request, 'homechefapp/for_you.html', context)


#####################################_____ABOUT VIEW______#####################################
def about(request):
    return render(request, 'homechefapp/about.html', {'webPageTitle': 'About'})


#####################################_____HOME VIEW______#####################################
def home(request):
    response = requests.get(randomUrl)
    data = response.json()
    homeRecipes = data['recipes']

    context = {
          'recipes' : homeRecipes,
           'webPageTitle' : 'Home',
    }

    return render(request, 'homechefapp/home.html', context)

