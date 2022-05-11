from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.forms import IntegerField
from datetime import datetime

# the models used so far are not final and are up for revision

# ***USER MODEL IS ALREADY BUILT-IN to DJANGO, so no need to create a user model***

class Comment(models.Model):
    user = models.ForeignKey(User, default='', on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField(null=True)
    recipe_id = models.IntegerField(default=0)
    title = models.CharField(max_length=10000, default='')
    created_on = models.DateTimeField(default=datetime.now())
    #created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} Comment'
    

class rating(models.Model):
    #add one to hold user id of the rater here
    #add one for the rating (from 1 to 5)
    pass;

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        #resize image
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)