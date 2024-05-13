def power(n,r):
    solve=1
    for i in range(r):
        solve *= n
    return solve
print(power(6,2))