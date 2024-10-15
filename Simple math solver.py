#python script for math calculation.
import math as mt
import time

while 0<1:
    print("\n------------------\n")
    print("1.Area of circle\n2.Area of triangle\n3.Area of square\n4.Area of rectangle\n5.Circumference of circle\n6.Perimeter of Square\n7.Perimeter of a Rectangle\n8.Perimeter of a Triangle \n9.Exit \n\n------------\n ")
    choice=input("Choose options from abov list (Number): ")

    if choice=="1":
        r=float(input('Enter radius of circle :  '))
        print(f"Area of circle is {round((mt.pi*r**2),2)}")
    elif choice=="2":
        b=float(input("Enter breadth of Triangle : "))
        h=float(input("Enter height of Triangle : "))
        print(f"Area of triangle is {round(0.5*b*h)} ")
    elif choice=="3":
        s=float(input("Enter side of square : "))
        print(f"Area of square is {round(s**2)}")
    elif choice=="4":
        l=float(input("Enter length of rectangle : "))
        w=float(input("Enter width of rectangle : "))
        print(f"Area of rectangle is {round(l*w)}")
    elif choice=="5":
        r=float(input('Enter radius of circle :  '))
        print(f"Circumference of circle is {round(2*mt.pi*r)}")
    elif choice=="6":
        s=float(input("Enter side of square : "))
        print(f"Perimeter of square is {round(4*s)}")
    elif choice=="7":
        l=float(input("Enter length of rectangle : "))
        w=float(input("Enter width of rectangle : "))
        print(f"Perimeter of rectangle is {round(2*(l+w))}")
    elif choice=="8":
        a=float(input("Enter side of triangle : "))
        b=float(input("Enter another side of triangle : "))
        c=float(input("Enter another side of triangle : "))
        print(f"Perimeter of triangle is {round(a+b+c)} ")
    elif choice=="9":
        print("Exiting............")
        time.sleep(3)
        exit()
    else:
        print("Invalid choice choose again")
        time.sleep(3)