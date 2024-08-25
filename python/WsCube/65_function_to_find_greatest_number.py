"""
Write a python function to find max between three numbers
"""
def max_num(a,b,c):
    if a >= b and a >= c:
        print("Maximum Number: ",a)
    elif b >= a and b >= c:
        print("Maximum Number: ",b)
    else:
        print("Maximum Number: ",b)
max_num(12,87,32)