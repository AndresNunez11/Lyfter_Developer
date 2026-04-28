"""
Cree un programa con un numero secreto del 1 al 10. 
El programa no debe cerrarse hasta que el usuario adivine el numero.
Debe investigar cómo generar un número aleatorio distinto cada vez que se ejecute.
"""

import random
number = random.randint(1,10)
guessed = int(input("Please enter a number between 1 and 10: "))
while (number != guessed):
    guessed =int(input("Incorrect number. Please try again with a number between 1 and 10: "))
print(f"You have guessed the number {number}")


