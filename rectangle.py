class Rectangle:
    def area(self):
        length = 10
        breadth = 5
        print("Rectangle Area =", length * breadth)

class Circle:
    def area(self):
        radius = 7
        print("Circle Area =", 3.14 * radius * radius)

shapes = [Rectangle(), Circle()]
for shape in shapes:
    shape.area()