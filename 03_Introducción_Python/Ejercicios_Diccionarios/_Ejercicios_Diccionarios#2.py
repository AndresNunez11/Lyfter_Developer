
""""
Cree un programa que cree un diccionario usando dos listas del mismo tamaño, usando una para sus keys, y la otra para sus values.
Ejemplos:
list_a = [first_name, last_name, role]
list_b = [Alek, Castillo, Software Engineer]
→ {first_name: Alek, last_name: Castillo, role: Software Engineer}
"""

list_a = ['first_name', 'last_name', 'role']
list_b = ['Alek', 'Castillo', 'Software Engineer']
my_dict = {}

for item in range(len(list_a)):
    my_dict[list_a[item]] = list_b[item]

print(my_dict)

