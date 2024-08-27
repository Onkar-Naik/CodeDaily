"""
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. 
Iterate through each command in order and perform the corresponding operation on your list.

Sample Input 0

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
Sample Output 0

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
"""

if __name__ == '__main__':
    N = int(input())
    ls = []
    for i in range(1,N+1):
        j = input().split()
        if j[0] == "insert":
            ls.insert(int(j[1]),int(j[2]))
        elif j[0] == "print":
            print(ls)
        elif j[0] == "remove":
            ls.remove(int(j[1]))
        elif j[0] == "append":
            ls.append(int(j[1]))
        elif j[0] == "sort":
            ls.sort()
        elif j[0] == "pop":
            ls.pop()
        elif j[0] == "reverse":
            ls.reverse()