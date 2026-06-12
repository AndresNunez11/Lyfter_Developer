from vehicleclass import Vehicle


class Car(Vehicle):

    def __init__(self, brand, year, wheels, model):
        super().__init__(brand, year)
        self._wheels = wheels
        self._model = model

    def get_info(self):
        return (f'Detalles del Auto: \nMarca: {self._brand}\nAño:{self._year}\nRuedas:{self._wheels}\nModelo:{self._model}')