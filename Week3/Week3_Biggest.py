
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


def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    biggest_value = 0
    for iteration in aDict:
        
        if len(aDict[iteration]) >= biggest_value:
            biggest_key = str(iteration)
            biggest_value = len(aDict[iteration])
    return biggest_key

print(biggest(animals))
        

dict = {'a','b'}
def k(d):
    for key in d:
        return(key)
print (k(dict))
    