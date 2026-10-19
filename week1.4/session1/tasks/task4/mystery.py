# Week 4, Session 1

# You are given the function mystery_func. 
# Inspect the code in the function
# Your task is to write a corresponding docstring
# - what the function does 
# - what is the input data and type
# - what is the return value and type


# function implementation

def mystery_func(string):       # defines the data type      
    upper = 0                   # defines the upper case letter and lower case letters amount as 0 if there is a an upper letter or a lower 0+1
    lower = 0

    for ch in string:       # for is for a loop to go through the entire input of strings and if is used to check the strings
        if ch.isupper():      #  if its either an upper or lower case letter if so it counts them and adds 1 each time 
            upper += 1
        if ch.islower():
            lower += 1
    return (upper, lower) #returns the count of the upper and lower case letters


# testing

print(mystery_func("abc"))
print(mystery_func("The quick Brown Fox!"))
print(mystery_func("012345"))
print(mystery_func("ABC"))


# Can you predict the output of the following lines of code?
# Uncomment the lines of code one by one and run the program
# to see if you are right?

print(mystery_func("X")) # (1,0)
print(mystery_func("[2, 3]")) # (0,0)
