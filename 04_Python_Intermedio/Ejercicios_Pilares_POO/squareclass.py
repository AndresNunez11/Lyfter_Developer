from shapeclass import Shape

class Square(Shape):

    def __init__(self, side):
        self.side = side
        self.perimeter = 0
        self.area = 0 
    
    def calculate_area(self):
        self.area = self.side * self.side
        return self.area

    def calculate_perimeter(self):
        self.perimeter = (self.side * 4) 
        return self.perimeter
        