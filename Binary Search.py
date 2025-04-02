a = [30, 20, 40, 60, 70, 69]
a.sort()
print(a)
search=eval(input("enter the element to search:"))
start=0
stop=len(a)-1
while(start<=stop):
    mid=(start+stop)//2
    if(search==a[mid]):
        print("element found at", mid+1)
        break
    elif(search<a[mid]):
        stop=mid-1
    else:
        start=mid+1
else:
    print("element not found")