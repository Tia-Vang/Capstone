from django.db.models.signals import post_save
from .models import user
from .models import recipe
from .models import comment_section
from .models import comment
from .models import rating
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

'''
    User methods
'''
def create_user():
    #logic for making user goes here
    print("user created") #for debugging

def update_user():
    #logic for updating user goes here
    print("user updated") #for debugging

def login_user():
    #logic for loging a user in
    print("user logged in") #for debugging

def logout_user():
    #logic for logging out user goes here
    print("user logged out") #for debugging

def get_user():
    #logic for method that returns user object based on id number
    print("user was retrieved")

'''
    Recipie methods
'''
#recipe methods go here


'''
    comment section methods
'''


'''
    rating methods
'''
#created profiles for users created
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

#created profiles for users created
@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    instance.profile.save()
    