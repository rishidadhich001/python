a=int(input("Enter num1 : "))
b=int(input("Enter num2 : "))
GCD=1

for i in range(1,min(a,b)):
    if a%1==0 and b%1==0:
        GCD=i

print("GCD of ",a,"and",b,"is",GCD )