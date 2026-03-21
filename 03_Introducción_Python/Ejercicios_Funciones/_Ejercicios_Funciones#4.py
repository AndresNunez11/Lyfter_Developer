
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


