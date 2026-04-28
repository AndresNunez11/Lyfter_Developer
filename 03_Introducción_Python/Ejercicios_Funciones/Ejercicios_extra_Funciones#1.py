"""
Cree una función que reciba un texto y un carácter, y retorne cuántas veces aparece ese carácter en el texto
Ejemplo:
Entrada:
Copiar
programacion
Ingrese el carácter que desea buscar:
o
Salida:
Copiar
Se a encontrado 2 veces el carácter
"""

def input_word():
    word = input('Ingrese una palabra:')
    return word
def input_letter():
    letter = input('Ingrese la letra a buscar: ')
    return letter
def count_letter(word, letter):
    counter = 0
    for char in word:
        if(char == letter):
            counter += 1
    return counter
def main():
    quantity = count_letter(input_word(), input_letter())
    print(f'Se ha encontrado {quantity} veces el carácter')
main()

