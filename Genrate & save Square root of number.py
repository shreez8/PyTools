from csv import *
import math as mt 

num=int(input("Enter range of square root needed : "))
name=str(input("Enter name for file : "))

def squareroot(num):
    return round(mt.sqrt(num),2)

with open(f'{name}.csv','w') as f1:
    f1.write(f"Number,Its square root,\n")
    for i in range(num):
        f1.write(f"{i},{squareroot(i)},\n")