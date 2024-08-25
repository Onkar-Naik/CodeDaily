"""
Write a python program to print numbers (1 to 10) and sqaures as 
key and value
"""
a = {}
for i in range(1,11):
    a[i] = i**2
print(a)