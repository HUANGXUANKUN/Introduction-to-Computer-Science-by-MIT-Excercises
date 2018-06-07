def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """
    # Your code here
    dict_store = {}
    result = None
    for element in L:
        try:
            dict_store[element] += 1
        except KeyError:
            dict_store[element] = 1
            
    dict_list = sorted(dict_store.keys())
    for element in dict_list:
        if dict_store[element] %2 != 0:
            result = element
            
    return result


                
    
            
            