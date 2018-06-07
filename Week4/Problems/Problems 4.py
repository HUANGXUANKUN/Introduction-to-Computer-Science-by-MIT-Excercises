# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 02:52:54 2018

@author: User
"""

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    # TO DO... <-- Remove this comment when you code this function
    handset = hand.values()
    handcount = 0
    
    for num in handset:
        handcount += num
        
    return handcount

print(calculateHandlen({'a':4,'g':0,'b':1}))