def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the 
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    result = ''
    for char in s:
        if char not in vowels:
            result += char
    print(result)

print_without_vowels("This is great!")
print_without_vowels("a")
            