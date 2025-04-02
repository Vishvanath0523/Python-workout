a = [20, 30, 40, 50, 60, 70, 80]
print(a)
search=eval(input("enter a element to search:"))
for i in range(0,len(a),1):
    if(search==a[i]):
        print("element found at", i+1)
        break
    else:
        print("element not found")