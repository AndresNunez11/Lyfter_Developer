class Rectangule:
    def __init__(self):
        self.width = no_negative_number(int(input(f"Ingrese el ancho: ")))
        self.height = no_negative_number(int(input(f"Ingrese la altura: ")))
        self.area = self.get_area()
        self.perimeter = self.get_perimeter()
    
    def get_area(self):
        try:
            return int(self.width) * int(self.height)
        except Exception as e:
            print(f'Error al calcular el area del rectandulo') 

    def get_perimeter(self):
        try:
            return int(self.height)*2 + int(self.width)*2
        except Exception as e:
            print(f'Error al calcular el perimetro del rectandulo')
    
#Clase para que el numero ingresado no sea negativo
class negativeTypeError(Exception):
    def __init__(self):
        super().__init__(f'\n Existe un valor negativo, los valores deben ser positivos')

# Exception Negative Number
def no_negative_number(enter_number):
    if enter_number < 0:
        raise negativeTypeError
    return enter_number