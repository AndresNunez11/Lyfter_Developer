class Personalinfo:

    def __init__(self, name, lastname):
        self._name = name 
        self._lastname = lastname


    # Por ser programacion orientada a objetos se utiliza el staticmethod para accederlo desde otra clase como decorador 
    @staticmethod
    def print_info(func):
        def wrapper(self, name, lastname, **kwargs):
            print(f'Nombre: {name}')
            print(f'Apellido {lastname}')
            for key, value in kwargs.items():
                print(f"{key}: {value}")
            result = func(self, name, lastname, **kwargs)
            print(f'Retorno: {result}')
            return result
        return wrapper

        


