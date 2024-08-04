"""
Write a python program to print sum of first 10 odd numbers 
"""
sum=0
n=0
while n < 20:
    if n % 2 == 1:
        sum += n
    n += 1
print(sum)