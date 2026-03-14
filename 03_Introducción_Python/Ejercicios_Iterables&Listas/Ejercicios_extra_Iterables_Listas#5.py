
"""
Cree un programa que le pida al usuario ingresar 5 palabras. 
Luego muestre una nueva lista con solo aquellas palabras que tengan más de 4 letras
"""

counter = 0
list = []
new_list = []

while(counter < 5 ):
    word = input('Ingrese una palabra ')
    list.append(word)
    counter+=1
print(f'Lista original \n {list}')
for data in list:
    if(len(data)>4):
        new_list.append(data)
print(f'La nueva lista con palabras que tienen mas de 4 letras es: \n {new_list}')

