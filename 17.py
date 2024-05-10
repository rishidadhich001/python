arr=[5,7,9,2,8,3]

a=0

print("Element of array : ")
for i in range(0,len(arr)):
    print(arr[i],end=' ')

for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if(arr[i]>arr[j]):
            a=arr[i]
            arr[i]=arr[j]
            arr[j]=a


print()

print("Element of ascending order : ")

for i in range(0,len(arr)):
    print(arr[i],end=' ')