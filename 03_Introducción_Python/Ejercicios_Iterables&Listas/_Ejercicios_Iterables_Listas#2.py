
"""
Cree un programa que itere e imprima un string letra por letra de derecha a izquierda.
Pista: investigue de que otras maneras se puede usar el range.
"""

my_string = 'Pizza con piña'

for index  in range(len(my_string)-1,-1,-1): #inicia del nuero mas alto en indice, se detiene en -1 y avanza de -1 en -1
    print(my_string[index])

