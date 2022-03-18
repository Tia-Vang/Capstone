from django.db import models

# the models used so far are not final and are up for revision

class user(models.Model):
    #this class will hold each user's data
    #so far, these feilds will each accept a sequence of charecters at most 100 in length
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    username = models.CharField(max_length = 100)
    #add one for user id
    #add one for preffernces here
    #add one for comments here


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
class comment(models.Model):
    #add one to hold the userid of the commentor
    body = models.CharField(max_length = 10000000)

class rating(models.Model):
    #add one to hold user id of the rater here
    #add one for the rating (from 1 to 5)
