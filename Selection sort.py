a = [16, 10, -1, 369, 5]
for i in range(len(a)):
    small = min(a[i:])
    index = a.index(small)
    a[i],a[index] = a[index],a[i]
print(a)