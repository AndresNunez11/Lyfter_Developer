class GreetUser:

    def __init__(self, name):
        self._name= name

    def print_info(self):
        print(f'Hola, {self._name}')
    
    @staticmethod
    def repeat_twice(func):
        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
                func(*args, **kwargs)
            except Exception as e:
                print(f'Error al imprimir dos veces. Error: {e}')
        return wrapper
    
    @repeat_twice
    def repeat_info(self):
        self.print_info()
    