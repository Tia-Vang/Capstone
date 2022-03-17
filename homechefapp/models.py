from django.db import models

# the models used so far are not final and are up for revision

class user(models.Model):
    #this class will hold each user's data
    #so far, these feilds will each accept a sequence of charecters at most 100 in length
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    username = models.CharField(max_length = 100)
