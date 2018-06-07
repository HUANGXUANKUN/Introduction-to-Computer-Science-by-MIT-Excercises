# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 02:32:46 2018

@author: User
"""

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    handcopy = hand.copy()
    if word in wordList:
        try:
            for letter in word:
                handcopy[letter] -=1
                if handcopy[letter] < 0:
                    return False
        except KeyError:
            return False
        else:
            return True
            
    else:
        return False
    