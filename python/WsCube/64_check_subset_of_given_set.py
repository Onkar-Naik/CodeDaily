"""
Write a python program to check set is subset of existing set or not
"""
a = {1,2,3,4,5,6,7,8,9}
b = {1,3,5,7,9}

if b.issubset(a):
    print("'b' is subset of 'a'")
else:
    print("'b' is not subset of 'a'")