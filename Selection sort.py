a = [16, 10, -1, 369, 5] #Create a list of integers
for i in range(len(a)): # Loop through each indx in the index
    small = min(a[i:]) # Find the smallest element in the unsorted portion of the list starting from the index i
    index = a.index(small) # Find the index of that smallest element in the entire list
    a[i],a[index] = a[index],a[i] #Swap the current element with the smallest element found
print(a) #After the loop exist ends, print the sorted list
