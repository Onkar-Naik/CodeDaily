"""
Write a python program to swap first and fourth element of the list
"""
a = [1,2,3,4,5,6,7,8]
print("List before swapping first and fourth elememt: ",a)
"""temp = a[0]
a[0] = a[3]
a[3] = temp"""
a[0],a[3] = a[3],a[0]
print("List after swapping first and fourth elememt: ",a)