"""
Write a python program to print smallest number of the list
"""
a = [12,32,53,643,21,4,13]
print("List: ",a)
"""small = a[0]
for i in a:
    if large < i:
        large = i
print("Largest number of the list is: ",large)"""
a.sort()
print("Smallest number of list: ",a[0])
