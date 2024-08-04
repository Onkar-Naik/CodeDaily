"""
Write a program to print ID card of student:
name, grade, age, email, phone number
"""

name = input("Enter a student's name:")
grade = input("Enter a student's Grade:")
age = int(input("Enter a student's age:"))
email = input("Enter a student's email:")
phone = input("Enter a student's phone number:")
print(f"""
Student ID Card
Name = {name}
Grade = {grade}
Age = {age}
Email = {email}
Phone No = {phone}
""")

