
"""
Cree un programa que itere e imprima los valores de dos listas del mismo tamaño al mismo tiempo.
"""

first_list = ['Hay', 'en', 'que', 'iteracion', 'indices', 'muy']
second_list = ['casos', 'los', 'la', 'por', 'es', 'util']
index=0

if(len(first_list)==len(second_list)):  
    while (index < len(first_list)):
        dato1 = first_list[index]
        dato2 = second_list[index]    
        print(f"{dato1} {dato2}")
        index+=1
else:
    print("Las listas no son del mismo tamaño")


first_list2 = ['Primera lista','Hay', 'en', 'que', 'iteracion', 'indices', 'muy']
second_list2 = ['y Segunda segunda','casos', 'los', 'la', 'por', 'es', 'util']

if(len(first_list2)==len(second_list2)):  
    for index in range(0, len(first_list2)):
        dato1 = first_list2[index]
        dato2 = second_list2[index]    
        print(f"{dato1} {dato2}")
else:
    print("Las listas no son del mismo tamaño")


"""
Cree un programa que itere e imprima un string letra por letra de derecha a izquierda.
Pista: investigue de que otras maneras se puede usar el range.
"""

my_string = 'Pizza con piña'

for index  in range(len(my_string)-1,-1,-1): #inicia del nuero mas alto en indice, se detiene en -1 y avanza de -1 en -1
    print(my_string[index])


"""
Cree un programa que intercambie el primer y ultimo elemento de una lista. 
Debe funcionar con listas de cualquier tamaño.
"""

my_list = [4, 3, 6, 1, 7]
counter = len(my_list)
index = 0
print(f'{counter}')
print(f"Antes \n{my_list} \n Despues \n")

for index in enumerate(my_list):
    if(index == 0):
        data = my_list[0]
        my_list[0] = my_list[counter-1]
        my_list[counter-1] = data
print(my_list)


"""
Cree un programa que elimine todos los números impares de una lista.

"""

'''
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list)
for index, data in enumerate(my_list):
    if(data%2 != 0):
        my_list.pop(index)
print(my_list) 
'''

'''
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,11,11,11]
my_list_even = []
print(my_list)
for index, data in enumerate(my_list):
    if(data%2 == 0):
        my_list_even.append(data)
print(my_list_even) 


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,11,11,11]
my_list_even = []
print(my_list)
for index, data in enumerate(my_list):
    if(data%2 == 0):
        my_list_even.append(data)
print(my_list_even) 

'''
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,11,11,11]
my_list_temp = []
my_list_even = []
len_list = len(my_list)

while(len_list >0):
    data = my_list.pop(len_list-1)
    if(data%2 == 0):
        my_list_temp.append(data)
    len_list -=1
large = len(my_list_temp)
while(large >0):
    my_list_even.append(my_list_temp[large-1])
    large -=1
print(my_list_even)






"""
Cree un programa que le pida al usuario 10 números, 
y al final le muestre todos los números que ingresó, 
seguido del numero ingresado más alto.
"""


my_list = []
counter = 0
largest_number = 0
while (counter < 10):
    number = int(input("Ingrese un numero: "))
    if(largest_number < number):
        largest_number = number
    my_list.append(number)
    counter+=1
print(f'La lista de nuemros ingresados es: {my_list} y el numero mayor es: {largest_number}')











