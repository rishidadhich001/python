number = 1

for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end="")
    number = 1  
    for k in range(1,i+1):
        print(' ', number, sep='', end='')
        number = number * (i - k) // k
    print()