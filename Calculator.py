#Basic calcualtor without any libaray used.

def addition(a,b):
    return a+b

def multiply(a,b):
    return a*b 

def substraction(a,b):
    return a-b 

def division(a,b):
    return a/b

print("Enter value for a and b :  ")
a=int(input("a: "))
b=int(input("b: "))

if int(a) & int(b):  
    print("Choose Operations to perform: ")
    print("1. Addition \n2.Substraction\n3.Multiplication\n4.Division\n--------")
    opt=int(input("Enter choice: "))

    if opt==1:
        value=addition(a,b)
        print('sum of {a} + {b} is ',value)
    elif opt==2:
        value=substraction(a,b)
        print('Substraction of {a} - {b} is ',value)
    elif opt==3:
        value=multiply(a,b)
        print('Multiplication of {a} * {b} is ',value)
    elif opt==4:
        value=division(a,b)
        print('division of {a} / {b} is ',value)
    else: 
        print("Invalid choice.")
else:
    print("Input is not Number.")