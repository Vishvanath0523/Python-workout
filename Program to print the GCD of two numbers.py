#Program to compute the GCD of two numbers
X = int(input("Enter the first number:"))
Y = int(input("Enter the second number:"))
if X > Y:
    smaller = Y
    
else:
    smaller = X
    
for i in range (1, smaller+1):
    if((X % i == 0) and (Y % i == 0)):
        gcd = i
    print("GCD is", gcd)