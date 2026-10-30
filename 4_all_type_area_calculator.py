# All Area Calculator - PF Program by Aneesha Ali

import math

print("--- ALL AREA CALCULATOR ---")
print("1. Rectangle")
print("2. Square")
print("3. Circle")
print("4. Triangle")
print("5. Parallelogram")

choice = int(input("Enter your choice (1-5): "))

if choice == 1:
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    area = length * width
    print(f"Area of Rectangle = {area}")

elif choice == 2:
    side = float(input("Enter side of square: "))
    area = side * side
    print(f"Area of Square = {area}")

elif choice == 3:
    radius = float(input("Enter radius: "))
    area = math.pi * radius * radius
    print(f"Area of Circle = {area:.2f}")

elif choice == 4:
    base = float(input("Enter base of triangle: "))
    height = float(input("Enter height of triangle: "))
    area = 0.5 * base * height
    print(f"Area of Triangle = {area}")

elif choice == 5:
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    area = base * height
    print(f"Area of Parallelogram = {area}")

else:
    print("Invalid choice! Please select 1-5")
