
"""
Cree un programa que intercambie el primer y ultimo elemento de una lista. 
Debe funcionar con listas de cualquier tamaño.
"""

my_list = [4, 3, 6, 1, 7]
counter = len(my_list)
index = 0
print(f'{counter}')
print(f"Antes \n{my_list} \n Despues \n")

for index in enumerate(my_list):
    if(index == 0):
        data = my_list[0]
        my_list[0] = my_list[counter-1]
        my_list[counter-1] = data
print(my_list)

