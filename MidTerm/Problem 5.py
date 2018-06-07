# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 04:04:59 2018

@author: User
"""

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    # Your code here
    Dict_value = {}
    Dict_value_once = []
    Dict_key_once = []
    
    for iteration in aDict.values():
        if iteration not in Dict_value:
            
            Dict_value[iteration] = 1
        else:
            Dict_value[iteration] = Dict_value[iteration] + 1
        
    
    for iteration in Dict_value:
        
        if Dict_value[iteration] == 1:
            Dict_value_once.append(iteration)
          
    
    for iteration in aDict:
        
        if aDict[iteration] in Dict_value_once:
            Dict_key_once.append(iteration)
    
    Dict_key_once.sort()
    return Dict_key_once
    
print(uniqueValues({1:3,2:2,3:3,4:3,5:2,6:8,7:7}))
            
        
        
        