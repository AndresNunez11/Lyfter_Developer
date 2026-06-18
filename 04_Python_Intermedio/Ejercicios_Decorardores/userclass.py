from  datetime import date, datetime

class User:

    def __init__(self, name, birthday):
        self._name = name
        self._birthday = datetime.strptime(
            birthday,
            "%Y-%m-%d"
            ).date()

    @property
    def age(self):
        today= date.today()
        return (
            today.year
            - self._birthday.year
            - (
                (today.month, today.day)
                    <(self._birthday.month, self._birthday.day)
                )
            )
    
    @staticmethod
    def major_age(func):
        def wrapper(self,user):
            if user.age >= 18:
                print(f'Su edad es {user.age}, Usuario {user._name} mayor de edad')
            else:
                raise ValueError("Usuario menor de edad, no puede ingresar al sistema.")
            return func(self,user)
        return wrapper

        

