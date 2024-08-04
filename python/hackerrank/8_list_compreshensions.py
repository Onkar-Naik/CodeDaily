"""
Let's learn about list comprehensions! 
You are given three integers x,y and z representing the dimensions of a cuboid along with an integer n. 
Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i+j+k is not equal to n. Please use list comprehensions rather than multiple loops, as a learning exercise.

Sample Input

1
1
1
2
Sample Output 

[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
"""
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    #x_list = [i for i in range(x+1)]
    #y_list = [j for j in range(y+1)]
    #z_list = [k for k in range(z+1)]
    #ls = []
    #for i in x_list:
    #    for j in y_list:
    #        for k in z_list:
    #            if i+j+k != n:
    #                ls.append([i, j, k])
    ls = [[i, j, k] for i in range(x+1)for j in range(y+1) for k in range(z+1) if i+j+k != n]
    print(ls)
