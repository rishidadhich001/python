row = 5

for i in range(1,row+1):
    for j in range(1,row+1):
        if j == 1 or j == row or i == 1 or i == row:
          print(j,end=" ")
        else:
           print(" ",end=" ")
    print()