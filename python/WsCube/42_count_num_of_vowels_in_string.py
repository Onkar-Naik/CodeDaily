"""
Write a python program to count of vowels in the string
"""

a = input("Enter a string: ")
count = 0
for i in a.lower():
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        count += 1
print("Count of vowels in a string is: ",count)
