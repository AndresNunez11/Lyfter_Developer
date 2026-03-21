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


