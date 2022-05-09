import numpy as np

THRESH = 5; #test this to aquire a good threshold

'''
method to update tags dictionary:
please make sure to pass in a dictionary where
key = tag
value = # times used (or weight of total uses)
and a list, tags, of all tags on a recipie

clicking a Recepie = 1 point

'''
def update_tags(tag_dict, tags):
    print("updated tags")
    for (i in tags):
        #if i in dict, update value

        #else, add key value pair: tag: points
        pass;

'''
method to get search terms:
please make sure to pass in a dictionary where
key = tag
value = # times used (or weight of total uses)

Cycles through the dictionary and, if a tag has a value
above the threshold, add it to the search terms

'''
def get_search_terms(tag_dict):
    print("got search tags")
