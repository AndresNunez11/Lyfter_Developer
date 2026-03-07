"""
Cree un diccionario que guarde la siguiente información sobre un hotel:
nombre
numero_de_estrellas
habitaciones
El value del key de habitaciones debe ser una lista, y cada habitación debe tener la siguiente información:
numero
piso
precio_por_noche
"""

my_dictionary ={
    'nombre':'Marriot',
    'numero_estrellas':4,
    'habitaciones':
    [
        {'numero':22,
        'piso':2,
        'precio_por_noche':20
        },
        {
        'numero':32,
        'piso':3,
        'precio_por_noche':25
        },
    ]
}
print(my_dictionary)

""""
Cree un programa que cree un diccionario usando dos listas del mismo tamaño, usando una para sus keys, y la otra para sus values.
Ejemplos:
list_a = [first_name, last_name, role]
list_b = [Alek, Castillo, Software Engineer]
→ {first_name: Alek, last_name: Castillo, role: Software Engineer}
"""

list_a = ['first_name', 'last_name', 'role']
list_b = ['Alek', 'Castillo', 'Software Engineer']
my_dict = {}

for item in range(len(list_a)):
    my_dict[list_a[item]] = list_b[item]

print(my_dict)


"""
Cree un programa que use una lista para eliminar keys de un diccionario.
Ejemplos:
list_of_keys = [access_level, age]
employee = {name: John, email: john@ecorp.com, access_level: 5, age: 28}
→ {name: John, email: john@ecorp.com}
"""

employee= {
    "name": "John", 
    "email": "john@ecorp.com", 
    "access_level": 5, 
    "age": 28
}
print(employee)
list_of_keys = ['access_level', 'age']

for key in list_of_keys:
    if key in employee:
        employee.pop(key)
print(employee)

