def newtonsqrt(n): #defining the variable 
    root = n/2 
    for i in range (20): # giving the range value 
        root = (root + n/root)/2 #applying the root function
    print(root) #getting the values from the root value
n = eval(input("Enter the square root of the number:")) #evaluating and printing the values
newtonsqrt(n) 
