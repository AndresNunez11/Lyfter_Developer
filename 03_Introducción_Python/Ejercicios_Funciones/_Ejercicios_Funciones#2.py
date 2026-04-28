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



