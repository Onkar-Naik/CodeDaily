""""
Write a program to sum of even numbers up to 50
"""
sum = 0
for i in range (2,51):
    if i%2 == 0:
        sum += i
print(sum)