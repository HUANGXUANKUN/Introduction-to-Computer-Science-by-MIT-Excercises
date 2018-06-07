s = 'azcbobobegghakl'
current = s[0]
store = s[0]  
for letter in s[1:]:
    if letter >= current[-1]:
        current += letter
        if len(current) > len(store):
            store = current
    else:
        current = letter
print('Longest substring in alphabetical order is: ' + str(store))    
        
    