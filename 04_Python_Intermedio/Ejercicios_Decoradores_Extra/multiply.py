from  datetime import datetime

class Multiply:

    def __init__(self, numebr1, number2):
        self.__number1 = numebr1
        self.__number2 = number2


    @property
    def multiply(self):
        return self.__number1 * self.__number2
    
    @staticmethod
    def validate_numbers(func):
        def wrapper(self, *args):
            try:
                float(args[0])
                float(args[1])
            except ValueError:
                raise ValueError("El dato ingresado debe ser un número")
            return func(self, *args)
        return wrapper


    @staticmethod
    def log_call(func):
        def wrapper(self, *args):
            print("\n--- LOG CALL ---")
            print(f"Función: {func.__name__}")
            print(f"Args: {args}")
            print(f"Fecha: {datetime.now()}")
            result = func(self, *args)
            print(f"Retorno: {self.multiply}")
            print("--- FIN LOG ---\n")
            return result
        return wrapper
            
        
        