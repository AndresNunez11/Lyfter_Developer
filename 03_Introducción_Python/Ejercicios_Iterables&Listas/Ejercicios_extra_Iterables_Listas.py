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

"""
Cree un programa que muestre el valor más pequeño de una lista sin usar min().
"""

my_list=[9,4,7,1,5]
minor_number=my_list[0]
counter = 0

for number in my_list:
    if(minor_number > number):
        minor_number = number
print(f'El menor valor es: {minor_number}')


"""
Cree un programa que reciba una lista de números y calcule el promedio de los valores, 
luego cree una nueva lista con solo los valores mayores al promedio
"""

largest_number = int(input('Indique el tamaño de la lista: '))
list = []
new_list= []
counter = 0
sum= 0

while(counter < largest_number):
    number=int(input('Ingrese un numero para la lista: '))
    sum= sum+number
    list.append(number)
    counter+=1
print(f'La lista completa es: {list}')
average= sum / largest_number

for index, data in enumerate(list):
    print(f'dato: {data} promedio: {average} index: {index}')
    if(data>average):
        new_list.append(data)
print(f'La lista solo con los numeros mayores al promedio de {average}\n nueva lista: {new_list}')




"""
Cree un programa que le pida al usuario ingresar 5 palabras. 
Luego muestre una nueva lista con solo aquellas palabras que tengan más de 4 letras
"""

counter = 0
list = []
new_list = []

while(counter < 5 ):
    word = input('Ingrese una palabra ')
    list.append(word)
    counter+=1
print(f'Lista original \n {list}')
for data in list:
    if(len(data)>4):
        new_list.append(data)
print(f'La nueva lista con palabras que tienen mas de 4 letras es: \n {new_list}')

