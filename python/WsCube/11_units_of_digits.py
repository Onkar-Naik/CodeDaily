"""
write a program to check number is single digit, two digit and so on.... up to 5 digits
"""

num = int(input("Enter a number:"))
if num >=0 and num < 10:
    print("It is single digit number")
elif num >=10 and num < 100:
    print("It is Two digits number")
elif num >=100 and num < 1000:
    print("It is Three digits number")
elif num >=1000 and num < 10000:
    print("It is Four digits number")
elif num >=10000 and num < 100000:
    print("It is Five digits number")
else:
    print("Number is out of range...!")