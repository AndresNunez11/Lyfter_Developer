import math
from shapeclass import Shape

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius
        self.perimeter = 0
        self.area = 0 
    
    def calculate_area(self):
        self.area = self.area = math.pi * (self.radius**2)
        return self.area

    def calculate_perimeter(self):
        self.perimeter = 2*math.pi *self.radius
        return self.perimeter