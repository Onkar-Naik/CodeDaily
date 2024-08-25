def prime(a):
    count = 0
    for i in range(2,a+1):
        if a % i == 0:
            count += 1
    if count >= 2 or a== 1:
        print(f"{a} is not prime number")
    else:
        print(f"{a} is prime number")
b = int(input("Enter a number:"))
prime(b)