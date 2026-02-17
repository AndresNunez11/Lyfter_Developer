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




"""
Cree una función que reciba una lista de palabras y un número n, y 
retorne una nueva lista con solo las palabras que tengan más de n letras
Ejemplo:
Entrada:
["cielo", "sol", "maravilloso", "día"]
Ingrese el numero de letras minimas en la palabra:  4
Salida:
["cielo", "maravilloso"]
"""

def my_list():
    words = ["cielo", "sol", "maravilloso", "día"]
    return words
def input_number():
    number = int(input('Ingrese el numero de letras minimas en la palabra: '))
    return number
def filter_words(words, number):
    new_list = []
    for word in words:
        if(len(word) > number):
            new_list.append(word)
    return new_list
def main():
    result = filter_words(my_list(), input_number())
    print(result)
main()



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