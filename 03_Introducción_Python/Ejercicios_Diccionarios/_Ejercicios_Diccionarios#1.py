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
