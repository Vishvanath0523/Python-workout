def newtonsqrt(n):
    root = n/2
    for i in range (20):
        root = (root + n/root)/2
    print(root)
n = eval(input("Enter the square root of the number:"))
newtonsqrt(n)
