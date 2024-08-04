""""
Write a program to swap two numbers without using third variable
"""

x = 11
y = 12
print(f"Values before swapping:x = {x} and y = {y}")
"""x = x+y #23
y = x-y #23-12 =11
x = x-y #23-11 =12"""
x,y = y,x #it can be achieved by assigning as well
print(f"Values after swapping:x = {x} and y = {y}")