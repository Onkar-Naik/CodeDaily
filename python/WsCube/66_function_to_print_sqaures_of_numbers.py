"""
Write a python program to print squares of numbers in a list from 1-30
"""
def list_of_squares():
    ls = []
    for i in range(1,31):
        ls.append(i**2)
    return ls
print(list_of_squares())