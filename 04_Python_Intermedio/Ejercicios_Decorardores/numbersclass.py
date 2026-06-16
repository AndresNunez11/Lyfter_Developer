class Numbers:

    @staticmethod
    def validate_numbers(func):
        def wrapper(*args):
            for item in args[1:]:  # Ignora self -- el primer argumento en menu es self
                try:
                    float(item)
                    print(f'{item} es un numero')
                except  ValueError as error:
                    print(f'Error: {error}\nDato ingresado no es un número. Intente nuevamente.')
                    return False
            result = func(*args)
            return result
        return wrapper