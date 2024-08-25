"""
Write a python program to check string contains all the digits
"""
a = input("Enter a string:")
print("Entered String:",a)
if a.isdigit():
    print("String contains only digits")
else:
    print("String does not contain only digits")