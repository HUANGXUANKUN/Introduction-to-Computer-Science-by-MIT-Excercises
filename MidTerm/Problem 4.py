

def lessThan4(aList):
    '''
    aList: a list of strings
    '''
    # Your code here
    result_list= []
    for iteration in aList:
        print(iteration)
        if len(iteration) < 4:
            result_list.append(iteration)
    return result_list