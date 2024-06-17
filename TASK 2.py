""" TASK 2 : CALCULATOR"""
"""DESIGNING A SIMPLE CALCULATOR WITH BASIC OPERATIONS.PROMPT THE USER TO INPUT TWO NUMBERS AND AN
OPERATION CHOICE.PERFORM THE CALCULATIONS AND DISPLAY RESULT."""

num1=float(input("Enter the Number="))
num2=float(input("Enter the Number="))

print("Enter choice 1 for addition")
print("Enter choice 2 for subtraction")
print("Enter choice 3 for multiplication")
print("Enter choice 4 for divison")

choices=int(input("Enter the choice from 1 to 4:"))
if choices==1:
    Sum=num1+num2
    print("sum of two numbers is =",Sum)
elif choices==2:
    diff=num1-num2
    print("Difference of two number is =",diff)
elif choices==3:
    mult=num1*num2
    print("Multiply of two number",mult)
elif choices==4:
    div=num1/num2
    print("divison of two numbers",div)
else:
    print("Invalid Input...Enter within the Range")


