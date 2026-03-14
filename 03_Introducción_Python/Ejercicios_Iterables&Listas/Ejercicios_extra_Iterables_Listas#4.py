
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

