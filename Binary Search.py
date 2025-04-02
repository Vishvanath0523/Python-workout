a = [30, 20, 40, 60, 70, 69] #create a list of integers
a.sort() #Sort the list in ascending order (required for binary search)
print(a) #Print the sorted list
search=eval(input("enter the element to search:")) # Take the insput fro the user and evaluate it as a python expression
start=0#intialiaze the start index for binary search
stop=len(a)-1 #Intialize the stop(end) index for binary search
while(start<=stop): #Begin the binary search loop while start index is less than or equal to stop loop.
    mid=(start+stop)//2 #Calculate the middle index
    if(search==a[mid]): #If middle element matches the search value, print the position (1-based) and exit the loop
        print("element found at", mid+1) #If the search value is less than the middle element , adjust the stop index to search the left half
        break
    elif(search<a[mid]): #if the search value is greater than the middle element, adjust start index to search the right half
        stop=mid-1
    else:
        start=mid+1
else:
    print("element not found") #if the element not found afte the loop ends, print the "Element not found"
