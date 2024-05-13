num1=int(input("Enter number : "))
sum=0

num2=num1

while num2>0:
    total=num2%10
    sum+=total**3
    num2//=10


if num1==sum:
        print("This number is  Armstrong number.....")
else:
    print("This number is not Armstrong number.....")