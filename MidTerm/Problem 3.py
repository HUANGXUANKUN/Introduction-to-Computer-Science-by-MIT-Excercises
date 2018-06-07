# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    # Your code here
    exp = 0
    
    while base**exp < num:
        exp += 1
    
    if base**exp == num:
        return exp
    
    else:
        diff_a = abs(num-(base**(exp-1)))
        diff_b = abs(num-(base**(exp)))
        
        if diff_a <= diff_b:
            return exp-1
        else:
            return exp
        
print(closest_power(4,62 ))
print(closest_power(4, 12))
print(closest_power(5,22 ))
print(closest_power(100, 1))
print(closest_power(2, 384.0))
print(closest_power(7, 196.0))
print(closest_power(10, 550.0))
        

            
        