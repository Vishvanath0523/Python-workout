def power(base,exp):
#Base case: If the exponent is 1, return the base
    if(exp==1):
        return (base)
    else:
        #Recursive case: Mulitply the base with the result of power(base, exp-1)
        return(base*power(base,exp-1))
#Taking input from the user for the base and exponent
base=int(input("Enter base:"))
exp=int(input("Enter the exponential value:"))
print("Result:", power(base,exp))
