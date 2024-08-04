"""
Write a program to find area of the square, rectangle, circle, triangle
"""
print("""
**********AREA CALCULATOR*************
      PRESS 1 FOR THE SQUARE
      PRESS 2 FOR THE RECTANGLE
      PRESS 3 FOR THE CIRCLE
      PRESS 4 FOR THE TRIANGLE      
""")
n = int(input("Enter a number:"))
if n == 1:
    side = float(input("Enter the side of the sqaure:"))
    print(f"Area of square is {side**2}")
elif n == 2:
    length = float(input("Enter the length of the rectangle:"))
    breadth = float(input("Enter the breadth of the rectangle:"))
    print(f"Area of rectangle is {length*breadth}")
elif n == 3:
    radius = float(input("Enter the radius of the circle:"))
    print(f"Area of circle is {(22/7)* (radius ** 2) }")
elif n == 4:
    base = float(input("Enter the base of the triangle:"))
    height = float(input("Enter the height of the triangle:"))
    print(f"Area of triangle is {0.5 * base * height }")
else:
    print("Wrong choice...!")