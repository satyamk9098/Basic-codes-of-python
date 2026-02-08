class Area:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        a = 3.14 * self.radius * self.radius
        print("Area of Circle:", a)


# ---- main program ----
radius = float(input("Enter the radius: "))
a1 = Area(radius)
a1.area()
