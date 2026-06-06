from vehicleclass import Vehicle

class Motorcycle(Vehicle):

    def __init__(self, brand, year,model, wheels, motor ):
        super().__init__(brand, year)
        self._wheels = wheels
        self._model = model
        self._motor = motor
    
    def get_info(self):
        print(f' Detalle de la motocicleta: \nMarca: {self._brand} \nModelo: {self._model}\nMotoe: {self._motor}')