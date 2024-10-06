while 1>0:
    print("Enter value for a and b: ")
    a=int(input("A: "))
    b=int(input("B: "))
    opt=int(input("Enter choice in numbers \n1.Addition\n2.Substraction\n3.Multiplication\n4.Division\n5.Quit\n----------\n"))
    if opt==1:
        print('Sum of {a} + {b} is ',a+b)
    elif opt==2:
        print('Substraction of {a} - {b} is ',a-b)
    elif opt==3:
        print('Multiplication of {a} * {b} is ',a*b)
    elif opt==4:
        print('Division of {a} / {b} is ',a/b)
    elif opt==5:
        exit()
    else:
        print("Invalid choice.")