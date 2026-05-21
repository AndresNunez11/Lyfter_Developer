

"""
Pasa los Ejercicios de Diagramas de flujo previamente creados a código:
Cree un diagrama de flujo que tenga un numero secreto del 1 al 10, 
y le pida al usuario adivinar ese número. El algoritmo no debe terminar 
hasta que el usuario adivine el numero.
"""

import random
number = random.randint(1,10)
guessed = int(input('Ingrese un numero entre 1 y 10: '))
while (number != guessed):
    guessed =int(input('NUmero incorrecto. Intente nuevamente con un numero de 1 a 10: '))
print(f'Has adivinado el numero {number}')

