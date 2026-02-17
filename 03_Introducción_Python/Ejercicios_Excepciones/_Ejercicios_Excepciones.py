"""
Cree una calculadora por linea de comando. Esta debe de tener un número actual, 
y un menú para decidir qué operación hacer con otro número:
1. Suma
2. Resta
3. Multiplicación
4. División
5. Borrar resultado
Al seleccionar una opción, el usuario debe ingresar el nuevo número a sumar, 
restar, multiplicar, o dividir por el actual. El resultado debe pasar a ser el nuevo numero actual.
Debe de mostrar mensajes de error si el usuario selecciona una opción invalida, 
o si ingresa un número invalido a la hora de hacer la operación.
"""

my_menu= [1,2,3,4,5,6]

def number1():
    while True:
        try:
            number1 = float(input('Ingrese primer numero: '))
            return number1
        except  ValueError as error:
            print(f'Error: {error}\nDato ingresado no es un número. Intente nuevamente.')
            
        

def number2():
    while True:
        try:
            number2 = float(input('Ingrese segundo numero: '))
            return number2
        except  ValueError as error:
            print(f'Error: {error}\n Dato ingresado no es un número. Intente nuevamente.')
        

def operator():
    while True:
        try:
            print('Seleccione la operacion a ejecutar')
            operator = int(input('1 (suma)\n2 (resta)\n3 (Multiplicación)\n4 (División)\n5 (CE Limpiar)\n6 (Salir)\n'))
            if(my_menu[0]<=operator<=my_menu[len(my_menu)-1]):
                return operator
            else:
                print(f'Debe ingresar un número entre 1 y {my_menu[len(my_menu)-1]}')
        except Exception as error:
            print(f'Error en el proceso.\n Debe ingresar un número entre 1 y {my_menu[len(my_menu)-1]}\n Intente nuevamente')
        

def sum (number1, number2):
    actual_number = number1 + number2
    return actual_number

def subtraction(number1, number2):
    actual_number = number1 - number2
    return actual_number

def division(number1, number2):
    actual_number = number1 / number2
    return actual_number

def multiplication(number1, number2):
    actual_number = number1 * number2
    return actual_number

def calculator(number1, operator, number2):
    while True:
        try:
            match operator:
                case 1:
                    actual_number = sum(number1, number2)
                    print(f'{number1} + {number2} = {actual_number}')
                    return actual_number
                case 2:
                    actual_number = subtraction(number1, number2)
                    print(f'{number1} - {number2} = {actual_number}')
                    return actual_number
                case 3:
                    actual_number = multiplication(number1, number2)
                    print(f'{number1} * {number2} = {actual_number}')
                    return actual_number
                case 4:
                    if number2 == 0:
                        print("Error: división entre cero")
                        actual_number = number1
                        return actual_number 
                    else:
                        actual_number = division(number1, number2)
                        print(f'{number1} / {number2} = {actual_number}')
                        return actual_number
        except Exception as error:
            print(f'Error en el proceso {error} \n digite "5" o "6" para reiniriar o salir')
            

def main():
    'actual_number = 0'
    start = True
    while True:
        try:            
            operator_calc = operator()
            if operator_calc == 6:
                print("Saliendo del programa...")
                break
            elif operator_calc == 5:
                start = True
                actual_number = 0
                print("Calculadora reiniciada")
                print(f'Numero actual {actual_number}')
                continue
            elif(start == True):
                actual_number = int(number1())
                start = False
            else:
                actual_number = int(actual_number)
                start = False
            print(f'Numero Actual es {actual_number}')
            second_number = number2()
            actual_number = calculator(actual_number, operator_calc, second_number)
            print(f'Numero Actual es {actual_number}')
        except Exception as error:
            print(f'Existe un error al procesar los datos {error}\n Intente nuevamente')

main()