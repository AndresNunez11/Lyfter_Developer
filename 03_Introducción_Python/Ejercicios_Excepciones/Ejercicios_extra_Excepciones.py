"""Cree un programa que:
Pida al usuario su nombre
Si el nombre es numérico (isdigit()), haga raise ValueError("El nombre no puede ser un número")
Ejemplo:
Entrada:
Ingrese su nombre:  
5
Salida:
El nombre no puede ser un número
Luego pida su edad
Si no es un número válido, capture el ValueError y muestre un mensaje
Ejemplo:
Entrada:
Ingrese su edad: 
cinco
Salida:
"Número no valido"
Si todo sale bien, imprima un mensaje: Hola <nombre>, su edad es <edad>
Ejemplo:
Entrada:
Ingrese su nombre: 
Jean Carlo
Ingrese su edad:
27
Salida:
Hola Jean Carlo,
su edad es 
27
"""
class nameTypeError(Exception):
    def __init__(self,name):
        super().__init__(f'\n El nombre no puede ser o incluir un número')


def get_name():
    while True:
        try:
            your_name = input('Ingrese su nombre:\n')
            for char in your_name:
                if(char.isdigit()):
                    raise nameTypeError(your_name)
            return your_name
        except nameTypeError as e:
            print(f"Error detectado: {e}")

def get_age():
    while True:
        try:
            number = int(input('Ingrese su edad: '))
            return number
        except ValueError as e:
            print(f'El valor ingresado no es un numero entero {e}')



def name_age():
    name = get_name()
    age = get_age()
    print(f'Hola {name}, su edad es {age}')




"""""
Cree una función convertir_a_entero(lista) que:
Reciba una lista de strings
Intente convertir cada elemento a entero usando int()
Use try-except para atrapar los errores ValueError
Si algún elemento no puede convertirse, mostrar "No se pudo convertir el elemento: <valor>" y continuar con los demás
Ejemplo:
Entrada:
my_list = ['4','hola','10','5.2']
Salida:
Resultado:4
convertido a
4
No se pudo convertir el elemento: hola
10 
convertido a
10
No se pudo convertir el elemento: 5.2
"""

my_list1 = ['4','hola','10','5.2']

def data_validate(data):
    try:
        number = int(data)
        print(f'{data} convertido a {number}')
    except ValueError as e:
            print(f'No se pudo convertir el elemento: {data} \n El valor ingresado no es un numero entero {e}')


def cycle(list):
    try:
        for item in list:
            data_validate(item)  
    except  IndexError as error:
        print(f'El indice a usar no existe en la lista. Error: {error}')
    except Exception as e:
        print('Error en el proceso')

"""
Cree una función sumar_valores(lista) que:
Reciba una lista de elementos (strings, enteros, flotantes mezclados)
Intente convertir cada elemento a tipo float
Si puede, sume el valor y muestre: "<valor> sumado correctamente"
Si no puede, muestre: "Elemento inválido: <valor>"
Al final, imprima la suma total
Ejemplo:
Entrada:
my_list = ['10', 'manzana','5.5','3', 'n/a']
Salida:
10.0
sumado correctamente
Elemento inválido: manzana
5.5
sumado correctamente
3.0
sumado correctamente
Elemento inválido: n/a
Total de la suma:
18.5
"""
my_list2 = ['10','manzana','5.5','3','n/a']

def validate(data):
    try:
        number = float(data)
        return number
    except ValueError as ve:
        print(f'Dato no se puede convertir en un numero flotante, error: {ve}')
    except Exception as e:
        print(f'Elemento inválido: {data}')

def sum_value(list):
    sum = 0
    try:
        for item in list:
            value = validate(item)
            if(value):
                sum =sum + value
                print(f'{value} Sumado Correctamente')
        print(f'Total de la suma:\n {sum}')
    except IndexError as error:
        print(f'El indice a usar no existe en la lista. Error: {error}')
    except Exception as e:
        print(f'Error en el proceso {e}')

def main():
    name_age()
    cycle(my_list1)
    sum_value(my_list2)    

main()