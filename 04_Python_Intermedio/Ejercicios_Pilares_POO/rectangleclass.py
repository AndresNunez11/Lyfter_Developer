from shapeclass import Shape

class Rectangule(Shape):

    def __init__(self, large, width):
        self.large = large
        self.width =  width
        self.perimeter = 0
        self.area = 0 
    
    def calculate_area(self):
        self.area = self.large * self.width
        return self.area

    def calculate_perimeter(self):
        self.perimeter = (self.large * 2) + (self.width *2)
        return self.perimeter