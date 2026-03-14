"""
Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.
“I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”
"""


def my_string():
    mystring = 'I love Nación Sushi'
    return mystring

def count_letter(string):
    count_capital=0
    count_lower=0
    for char in string:
        if(char.isupper()):
            count_capital+=1
        elif(char.islower()):
            count_lower+=1
    print(f'Cantidad de mayusculas = {count_capital} \n y cantidad de minusculas = {count_lower}')

count_letter(my_string())


