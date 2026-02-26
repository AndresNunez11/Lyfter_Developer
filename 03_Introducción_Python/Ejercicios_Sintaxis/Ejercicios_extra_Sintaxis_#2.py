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





