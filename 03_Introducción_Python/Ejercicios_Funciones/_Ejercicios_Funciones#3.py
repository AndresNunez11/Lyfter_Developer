"""
Cree una función que retorne la suma de todos los números de una lista.
La función va a tener un parámetro (la lista) y retornar un numero (la suma de todos sus elementos).
[4, 6, 2, 29] → 41
"""


def sum_list(list):
    index = 0
    large = len(list)
    sum=0
    while(index < large):
        sum = sum + list[index]
        index+=1
    return sum

def main():
    list = [4, 6, 2, 29]
    print(f'La suma corresponde a {sum_list(list)}')
main()

