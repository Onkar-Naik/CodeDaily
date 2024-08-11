"""
Write a python code to find the number is prime or not
"""
n = int(input("Enter a number:"))
if n <= 0:
    print("Number is not greater than 0")
elif n == 1:
    print("It is not prime nor composite number")
else:
    count = 0
    for i in range(1,n+1):
        if n % i == 0: count +=1
    if count <=2:
        print("It is prime number")
    else:
        print("It is composite number")