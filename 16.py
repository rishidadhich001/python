array=[3,4,5,6,70]

maximumNumber=array[0]

for i in range(len(array)):
    if array[i]>maximumNumber:
     maximumNumber=array[i]


print("Maximum number : ",maximumNumber)