from abc import ABC, abstractmethod

class Shape(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def calculate_perimeter():
        pass

    @abstractmethod
    def calculate_area():
        pass