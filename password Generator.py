"""TASK 4: PASSWORD GENERATOR"""
import random

uppercase_ltrz = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_ltrz = uppercase_ltrz.lower()
digits ="0123456789"
symbols = "!@#$%&*()/+-*"

upper, lower, nums, symb = True, True, True, True

all=""

if upper :
    all+=uppercase_ltrz
if lower :
    all+=lowercase_ltrz
if nums:
    all+=digits
if symb:
    all+=symbols
    
length = int(input("Enter length of Password (between: 8-14) 🔑: "))

if 8<= length<=14:
    password = "".join(random.sample(all,length))
    print("New Password: ",password)
else:
    print("Please set length of Password between 8 to 14")
