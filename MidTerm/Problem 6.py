def max_val(t): 
    """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """

    int_list = []
    def return_int_list(sequence):
        for iteration in sequence:
            print('iteration = ',iteration)
            if type(iteration) == int:
                int_list.append(iteration)    
            else:
                return_int_list(iteration)
        print('list =',int_list)
        return int_list

    result_list = return_int_list(t)
    result_list.sort()
    print('sorted list =',result_list)
    return result_list[-1]

print(max_val((5, (1,2), [[1],[2]])))