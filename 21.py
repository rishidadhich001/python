def addition(i,j):
    i+=j
    return i

def Substraction(i,j):
    i-=j
    return i

def Multipliaction(i,j):
    i*=j
    return i

def division(i,j):
    i/=j
    return i

def Modul(i,j):
    i%=j
    return i

def default(i,j):
   print("Incorrect option")



switcher={
    1:addition,
    2:Substraction,
    3:Multipliaction,
    4:division,
    5:Modul
}

def switch(operation):
    return switcher.get(operation,default)()

print('''you can perform operation
      1.Addition
      2.Substraction
      3.Multipliaction
      4.Division
      5.Modul''')

choice=int(input("Enter your choice : "))
print(switch(choice))