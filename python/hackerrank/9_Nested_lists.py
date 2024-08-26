"""
Given the names and grades for each student in a class of  students, 
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, 
order their names alphabetically and print each name on a new line.

Sample Input 0

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
Sample Output 0

Berry
Harry
"""
if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        ls = []
        name = input()
        score = float(input())
        ls.append(name)
        ls.append(score)
        records.append(ls)
records.sort(reverse=True)
grades= [grades for names, grades in records]
grades.sort()
sec_min = grades[0]
for i in grades:
    if sec_min < i:
        sec_min = i
        break
second_rank = [name for name,grade in records if grade == sec_min]
second_rank.sort()
for i in second_rank:
    print(i)