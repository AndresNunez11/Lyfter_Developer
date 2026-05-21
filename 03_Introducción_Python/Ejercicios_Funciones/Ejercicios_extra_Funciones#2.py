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


