import math as mt 

def squareroot():
    num=float(input("Enter number to find its sqaure root : "))
    print(f"Square root of {num} is {round(mt.sqrt(num),2)}")
    

while 0<1:
    print("\n---------------\n1.Find square root of number\n2.Exit\n")
    c=(input("Enter ur Choice : "))
    if c=="1":
        squareroot()
    elif c=="2":
        exit()
    else:
        print("Invalid choice. Try again.")
    
