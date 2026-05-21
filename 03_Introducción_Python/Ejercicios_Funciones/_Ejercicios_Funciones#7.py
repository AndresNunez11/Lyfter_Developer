"""
Cree una función que acepte una lista de números y retorne una lista con 
los números primos de la misma.
[1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]
Tip 1: Investigue la logica matematica para averiguar si un numero es primo, y conviertala a codigo.
No busque el codigo, eso no ayudaria.
Tip 2: Aquí hay que hacer varias cosas (recorrer la lista, revisar si cada numero es primo, 
y agregarlo a otra lista). Así que lo mejor es agregar otra función para revisar si el numero 
es primo o no.
"""

def number_list():
    my_list = [1, 4, 6, 7, 13, 9, 67]
    return my_list

def primary_number(number):
    counter = 2
    while counter < number:
        if(number%counter == 0):
            break
        counter+=1
    if(counter == number):
        return number    
    

def list_primary_numbers(list):
    new_list = []
    index = 0
    while index < len(list):
        number = primary_number(list[index])
        if(number!= None):
            new_list.append(number)        
        index+=1        
    print(new_list)
    
list_primary_numbers(number_list())


