"""
Write a program to calculate area of different shapes
like square, rectangle, circle and triangle
"""

choice = int(input(
"""Enter a choice number from below to calculate area:
1.Square
2.Rectangle
3.Circle
4.Triangle"""))
if choice == 1:
    side = float(input("Enter a side of square:"))
    print("Area of square is:",side*side)
elif choice == 2:
    length =  float(input("Enter a length of the rectangle:"))
    breadth = float(input("Enter a breadth of the rectangle:"))
    print("Area of rectangle is:",length*breadth)
elif choice == 3:
    radius = float(input("Enter a radius of the circle:"))
    print("Area of circle is:", (22/7)* radius**2)
elif choice == 4:
    base = float(input("Enter base of a triangle:"))
    height = float(input("Enter height of a triangle:"))
    print("Area of triangle is:" , 0.5 * base *height)
else:
    print("Wrong choice")