"""
Cree un programa que cuente cuántas veces aparece un número específico en una lista. 
Pida al usuario una lista de números y otro número a buscar
"""


quantity = int(input("Indique la cantidad de numero a ingresar: "))
list = []
counter = 0 
counter_data =0
while(counter < quantity):
    number= int(input("Ingrese un numero: "))
    list.append(number)
    counter+=1
print(list)
search_data = int(input("Ingrese el numero a buscar: "))
for index, data in enumerate(list):
    if(data == search_data):
        counter_data+=1
print(f'El numero {search_data} se encuentra {counter_data} veces en la lista')

