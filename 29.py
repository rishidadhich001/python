def sum(n):
    if(n==0):
        return 0
    return (n % 10 + sum(int(n / 10)))
n = 12345
result = sum(n)
print("Sum of digits in",n,"is", result)