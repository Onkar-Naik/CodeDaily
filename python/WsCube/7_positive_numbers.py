"""
Write a python program to check number is positive or not
"""
n = int(input("Enter a number:"))
if n == 0:
    print("Number is neither positive nor negative")
elif n > 0:
    print("Number is Positive")
else:
    print("Number is Negative")