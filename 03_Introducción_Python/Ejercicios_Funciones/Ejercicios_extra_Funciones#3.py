"""
Cree una función que reciba un string y retorne cuántas vocales contiene
Ejemplo:
Entrada:
"Hola mundo"
Salida:
4
"""

def my_string():
    string =  'Hola Mundo'
    'input(Ingrese un texto:)'
    return string
def count_vowels(string):
    vowels = 'aeiouAEIOU'
    counter = 0
    for char in string:
        if char in vowels:
            counter += 1
    return counter
    
def main():
    result = count_vowels(my_string())
    print(result)   
main()