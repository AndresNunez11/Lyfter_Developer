import math


class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.area = 0

    def circle_area (self):
        print(self.radius)
        self.area = math.pi * (self.radius**2)
        print(f' El area del circulo es {self.area}') 


        



        

