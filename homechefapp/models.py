from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# the models used so far are not final and are up for revision

# ***USER MODEL IS ALREADY BUILT-IN to DJANGO, so no need to create a user model***

class recipe(models.Model):
    #this class will hold each user's data
    #so far, these feilds will each accept a sequence of charecters at most 100 in length
    title = models.CharField(max_length = 100)
    body = models.CharField(max_length = 1000000)
    url = models.CharField(max_length = 10000000) #should hold a shareable url of the recipie
    #add one for tags (keywords to search for) here
    #add one for image here
    #add one for ratings here
    #add one for view blocks (f a user choses not to see this one)
    #add one for reports
    #add one for comments

class comment_section(models.Model):
    #add an array or hash set to to hold all the comments
    pass;
class comment(models.Model):
    #add one to hold the userid of the commentor
    user = models.OneToOneField(recipe, related_name="comment", on_delete=models.CASCADE)
    title = models.CharField(max_length = 100)
    body = models.CharField(max_length = 100)

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