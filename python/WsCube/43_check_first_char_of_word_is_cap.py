"""
Write a python program to check words of a starts with capital letter
"""
a = input("Enter a line:")
print("Entered line: ",a)
if a.istitle():
    print("It is a title")
else:
    print("It is not a title")