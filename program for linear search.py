a = [20, 30, 40, 50, 60, 70, 80] #create a list of integers
print(a) #print the list to the integers
search=eval(input("enter a element to search:"))#Take the input from the user and evaluate it as a python expression
for i in range(0,len(a),1): # Loop through each integers of the list.
    if(search==a[i]):#check if the current element matches the search values
        print("element found at", i+1) #If found, print the index (1-based) where the element is found and exit the loop
        break
    else:
        print("element not found")#if not found at current index, print "element not found"
