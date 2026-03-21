
"""
Tabla de multiplicar personalizada
Pida al usuario un número del 1 al 10
Muestre su tabla de multiplicar del 1 al 12
"""

counter = 1
number= int(input("Ingrese un numero: "))

while(counter<=12):
    multiplication = number *counter
    print(f'{number} x {counter} = {multiplication}')
    counter=counter+1