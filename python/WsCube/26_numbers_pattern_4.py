"""
Write a program to print below number pattern
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1
"""
for i in range(1,6):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()