def intersection(array1,array2):
         array3=[value for value in array1 if value in array2]
         return array3
array1=[4,5,6,7,8,8]
array2=[9,8,7,6,5,6]      
print(intersection(array1,array2))     