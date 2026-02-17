
"""
Pasa los Ejercicios de Pseudocodigo previamente creados a código:
Cree un pseudocódigo que le pida un precio de producto al usuario, 
calcule su descuento y muestre el precio final tomando en cuenta que:
Si el precio es menor a 100, el descuento es del 2%.
Si el precio es mayor o igual a 100, el descuento es del 10%.
Ejemplos:
120 → 108
40 → 39.2
"""


price = float(input('Ingrese el precio del Producto: '))
if(price < 100):
    final_price = price - (price * 0.02 )
elif(price >= 100):
    final_price = price - (price * 0.10)
print(f'El precio final es de {final_price}')





"""
Cree un pseudocódigo que le pida un tiempo en segundos 
al usuario y calcule si es menor o mayor a 10 minutos. 
Si es menor, muestre cuantos segundos faltarían para llegar a 10 minutos. 
Si es mayor, muestre Mayor. Si es exactamente igual, muestre Igual.
Ejemplos:
1040 → Mayor
140 → 460
600 → Igual
599 → 1
"""

seconds =int(input('Ingrese la cantidad de segundos'))

if(seconds > 600):
    print('Mayor')
elif(seconds == 600):
    print('igual')
else:
    missing_seconds = 600 - seconds
    print(f'Los segundos faltantes para 10 minutos son: {missing_seconds}')





"""
Cree un algoritmo que le pida un numero al usuario, 
y realice una suma de cada numero del 1 hasta ese número ingresado. 
Luego muestre el resultado de la suma.
5 → 15 (1 + 2 + 3 + 4 + 5)
3 → 6 (1 + 2 + 3)
12 → 78 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12)
"""


counter = 0
sum = 0
number = int(input('Ingrese un numero '))
while(counter<number):
    counter=counter+1
    sum=sum+counter
print(f'La suma final de {number} corresponde a {sum}')



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



"""
Cree un diagrama de flujo que pida 3 números al usuario. 
Si uno de esos números es 30, o si los 3 sumados dan 30, 
mostrar Correcto. Sino, mostrar incorrecto.
Ejemplos:
23, 30, 768 → Correcto (hay un 30)
10, 15, 5 → Correcto (10 + 15 + 5 = 30)
35, 56, 2 → Incorrecto (no hay ningún 30, y la suma de ellos tampoco da 30)
"""


firts = int(input('Ingrese primer numero: '))
second = int(input('Ingrese segundo numero: '))
third= int(input('Ingrese tercer numero: '))
if(firts == 30 or second ==30 or third==30):
    print(f'Correcto, hay un 30 entre los 3 numeros')
elif(firts + second + third == 30):
    print(f'Correcto, la suma de los 3 numeros es 30')
else:
    print(f'Incorrecto, no hay ningún 30, y la suma de ellos tampoco da 30')


"""
Convertidor de unidades de temperatura
Pida al usuario ingresar una temperatura en Celsius
Conviértala a Fahrenheit y Kelvin
Muestre los tres valores
Ejemplo:
Entrada:
"Ingrese temperatura en Celsius:"
25
Salida:
Copiar
Fahrenheit
77.0
Kelvin
298.15
"""

celsius = float(input("Ingrese temperatura en Celsius: "))  
Fahrenheit= celsius*3.08
Kelvin= celsius * 11.926
print(f'{celsius} grados celsius corresponde a:\n{Fahrenheit} grados Fahrenheit y {Kelvin} grados Kelvin')


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