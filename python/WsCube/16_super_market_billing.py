"""
Write a program for billing system in supermarket for multiple customers
"""
print('*'*40)
print("Welcome to Super Market")
print('*'*40)
while True:
    name = input("Enter Customer Name:")
    total = 0
    while True:
        price = float(input("Enter the ammount:"))
        quantity = float(input("Enter the quantity:"))
        total += price*quantity
        repeat = input("Do you want to add anything(Y/N):")
        if repeat.upper() == "N":
            break
    print(f"Name:{name}")
    print(f"Total:{total}")
    repeat = input("Do you want continue with new customer(Y/N):")
    if repeat.upper() == "N":
        print("Thanks for shopping")
        print("*"*40)
        break
        

        