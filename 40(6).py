char = 65

for i in range(1, 6):
    for j in range(5 - i):
        print("  ", end="")
        
    for k in range(1, 2*i):
        if(k==1 or i==5 or k==2*i-1):
            print(chr(char),'', end="")
        else:
            print("  ", end="")
        char += 1
    char = 65
    print()