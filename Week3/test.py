# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 00:25:56 2018

@author: User
"""

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    num = 0
    for iteration in aDict.values():
        if len(iteration) > 1:
            num += len(iteration)
        else: 
            num += 1
    return num

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print(how_many(animals))