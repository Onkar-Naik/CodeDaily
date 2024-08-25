"""
Write a python program to print largest number of the list
"""
a = [12,32,53,643,21,4,13]
print("List: ",a)
"""large = a[0]
for i in a:
    if large < i:
        large = i
print("Largest number of the list is: ",large)"""
a.sort()
print("Largest number of list: ",a[-1])
