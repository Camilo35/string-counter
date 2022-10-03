def solutions(a,b):
    """Function wich counts how many times is a string inside another"""
    if a in b: # see if a is in b
        for j in a: # if a is a tuple then we take each element in it
            if j in b: # see if each element of 'a' variable is in b                
                counter = b.count(j)# create a counter
    else:        
        counter = 0    

    return counter


a='z' # assign random values for 'a' variable
b='abccbaaab' # assign random values for 'b' variable
counter=solutions(a,b) # call the function
print(counter) #verify if function works