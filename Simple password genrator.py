# Importinng string libraries for easy access of strings, random is for pickig random string.
from string import ascii_letters,digits,punctuation
import random

st=ascii_letters+digits+punctuation #storing need string into single varible.
password_len=int(input("Enter length of password to be generated (default=8) : \n")) #for taking user input.

def genrate_pass(password_len): #function for genrating password and make it easy to access.
    password=''
    for i in range(password_len):
        store=random.choice(st)
        password=password+store
    return password

if password_len<=8: #making sure password length is greater than 8 if less setting it to default number 8.
    password_len=8
    print(genrate_pass(password_len))
else:
    print(genrate_pass(password_len))
