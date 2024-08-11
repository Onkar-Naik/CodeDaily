"""
Write a prgram to print fibonacci series for 10 numbers
"""

first = 0
second = 1
print(first)
print(second)
for i in range(2,11):
    sum = first+second
    first = second
    second = sum
    print(sum)