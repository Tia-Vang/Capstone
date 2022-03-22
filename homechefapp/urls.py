
from django.urls import path, include
from .import views



urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('results/', views.search, name='results'),
    path('foryou/', views.for_you, name='tailored'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('about/', views.about, name='about'),
    path('', views.home, name='home'),
]
