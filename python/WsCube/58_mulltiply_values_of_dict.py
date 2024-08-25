"""
Write a python program to print multiplication of values of a dictionary
"""
a = {"one":1,"two":2,"three":3,"four":4}
mul = 1
for i in a:
    mul *= a[i]
print("Multiplication of values is: ",mul)