import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, variable):
        return self.x == variable.x and self.y == variable.y
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
    def distance(self, variable):
        return math.sqrt(((self.x - variable.x) ** 2) + ((self.y - variable.y) ** 2))
    
class Vector(Point):
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
        
    def __add__(self, variable):
        return Vector(self.x + variable.x, self.y + variable.y)
        
p1 = Point(1, 3)
p2 = Point(2, 4)
v1 = Vector(2, 5)
v2 = Vector(4, 3)

print("Does ", p1, " == ", p2, "? ", p1 == p2)
print("Distance between the two points: ", p1.distance(p2))
print("Vector 1: ", v1)
print("Vector 2: ", v2)
print("Vector sum: ", v1 + v2)