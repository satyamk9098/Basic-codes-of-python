#Area of Triangle (1/2 * base * height)
def area_of_triangle(base, height):
    return 0.5 * base * height

base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

print("Area of triangle:", area_of_triangle(base, height))