#List of numbers
a=[25,9,55,12,5]
#Initialize max variable to store the maximum numbers
max=0
#loop through each element in the list
for i in a:
    if (max < i): 
        max = i#update the max if the current element is greater

#Find and print the maximum number
print("maximum number=", max)
