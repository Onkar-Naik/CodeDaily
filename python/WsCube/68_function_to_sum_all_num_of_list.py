"""
Write a python program to print sum of all numbers of list
"""
def sum_of_list(a):
    sum = 0
    for i in a:
        sum += i
    return sum
list_a =[1,2,3,4,5,6,7,8,9,10]
print(sum_of_list(list_a))