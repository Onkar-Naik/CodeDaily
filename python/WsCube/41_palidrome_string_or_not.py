"""
Write a python program to check given string is palindrome or not
"""
a = input("Enter a string:")
print("Entered string: ",a)
b = a[::-1]
if a == b:
    print("It is palindrome")
else:
    print("It is not palindrome")