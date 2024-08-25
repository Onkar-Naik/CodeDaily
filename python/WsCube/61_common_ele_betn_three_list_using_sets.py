"""
Write a python code to find common elements between three list using sets
"""
a = [1,2,3,4,5]
b = [1,3,5,7,9]
c = [2,3,5,7,11]
print(set(a) & set(b) & set(c))