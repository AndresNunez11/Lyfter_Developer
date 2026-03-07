"""
1-Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda.
"""

def print_first():
    print('Imprime desde la primera funcion')
def print_second():
    print('Imprime la segunda funcion y luego:')
    print_first()
print_second()


"""
2-Experimente con el concepto de scope:
    Intente accesar a una variable definida dentro de una función desde afuera. 
    Intente accesar a una variable global desde una función y cambiar su valor.
"""



def firts_function():
    nombre = input('Cual es tu nombre: ')
    return nombre
def second_function():
    print(f'Hola {firts_function()} como estas ?')
second_function()

global_data = 'programa'
def program_name():
    name = 'Program # 1'
    global global_data 
    global_data= name
    print(global_data)
program_name()
'global_data =modificar la global real'
print(global_data)




"""
Cree una función que retorne la suma de todos los números de una lista.
La función va a tener un parámetro (la lista) y retornar un numero (la suma de todos sus elementos).
[4, 6, 2, 29] → 41
"""


def sum_list(list):
    index = 0
    large = len(list)
    sum=0
    while(index < large):
        sum = sum + list[index]
        index+=1
    return sum

def main():
    list = [4, 6, 2, 29]
    print(f'La suma corresponde a {sum_list(list)}')
main()


"""
Cree una función que le de la vuelta a un string y lo retorne.
Esto ya lo hicimos en iterables.
“Hola mundo” → “odnum aloH”
"""


def str_var ():
    msg = 'Hola Mundo'
    return msg 

def reverse_string(string):
    new_str=''
    for char in string:
        new_str = char+new_str
    print(new_str)

reverse_string(str_var())


"""
Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.
“I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”
"""


def my_string():
    mystring = 'I love Nación Sushi'
    return mystring

def count_letter(string):
    count_capital=0
    count_lower=0
    for char in string:
        if(char.isupper()):
            count_capital+=1
        elif(char.islower()):
            count_lower+=1
    print(f'Cantidad de mayusculas = {count_capital} \n y cantidad de minusculas = {count_lower}')

count_letter(my_string())



"""
Cree una función que acepte un string con palabras separadas por un guión y retorne un string 
igual pero ordenado alfabéticamente.
Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
“python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”
"""


def convert_string():
    my_string = 'python-variable-funcion-computadora-monitor'
    print(f'Cadena original es: {my_string}')
    return my_string

def alphabetic_order(string):
    my_list = string.split("-")
    my_list.sort()
    index = 0
    new_word=''
    while (index < len(my_list)):
        if(new_word == ''):
            new_word = my_list[index]
        else:
            new_word= new_word+'-'+my_list[index]
        index+=1
    print(f'La nueva cadena ordenada es {new_word}')

alphabetic_order(convert_string())



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


