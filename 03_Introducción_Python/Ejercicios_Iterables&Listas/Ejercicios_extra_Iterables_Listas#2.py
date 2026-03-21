
"""
Cree un programa que verifique si todos los elementos de una lista son positivos
Restricciones:
No use funciones como all()
"""

my_list = [5,6,-2,0,4]
counter = 0

for number in my_list:
    if(number < 0):
        print("Hay al menos un número negativo o cero")
        counter+=1
        break
if(counter == 0):
    print("No hay numeros menores o iguales a cero ")

