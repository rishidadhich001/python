def natural_number_sum(i):
    sum=0
    count=1


    while count<=i:
        sum=sum+count
        count+1

        return sum
    
i=int(input("Enter number : "))
total=natural_number_sum(i)
print("The sum of natural number is : ",total)