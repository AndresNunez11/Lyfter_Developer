from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def __init__(self, brand, year):
        self._brand = brand
        self._year = year
    
    @abstractmethod
    def get_info(self):
        return(f'Datos del Vehiculo: \nMarca: {self._brand} \nAño: {self._year} ')