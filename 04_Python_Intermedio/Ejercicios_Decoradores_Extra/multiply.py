from  datetime import datetime

class Multiply:

    def __init__(self, number1, number2):
        self.__number1 = number1
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
            result = func(self, *args)
            print("\n--- LOG CALL ---")
            print(f"Función: {func.__name__} Args: {args} Fecha: {datetime.now()} Resultado: {result}")
            print("--- FIN LOG ---\n")
            return result
        return wrapper
            
        
        