

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

