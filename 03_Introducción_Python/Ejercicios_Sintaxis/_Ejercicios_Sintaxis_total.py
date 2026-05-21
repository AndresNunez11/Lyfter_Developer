'''
Experimente haciendo sumas entre distintos tipos de datos y apunte los resultados.
Si le salen errores, no se asuste. Lealos e intente comprender qué significan.
Los errores son oportunidades de aprendizaje.
Por ejemplo:
string + string → ?
string + int → ?
int + string → ?
list + list → ?
string + list → ?
float + int → ?
bool + bool → ?
'''

string = 'test string'
string2= 'test string2'
number = 2
list1 =[1,2,3,4]
list2 = ['andres', 'jose', 'pablo', 'pedro']
list3 = [4,5,6,7]
decimal_number = 123.1234
bool1 = True
bool2 = False
bool3 = True
bool4 = False

'''
"string + string → ?"
print(string+string2) 
"= prueba stringprueba string2"

"string + int → ?"
print(string+number)
"= TypeError: can only concatenate str (not "int") to str"

"int + string → ?"
print(number+string)
"= TypeError: unsupported operand type(s) for +: 'int' and 'str'"

"list + list → ?"
print(list1 + list3) 
"=[1, 2, 3, 4, 4, 5, 6, 7]"
print(list1+list2)
"[1, 2, 3, 4, 'andres', 'jose', 'pablo', 'pedro']"

"string + list → ?"
print(string+ lista3)
"= TypeError: can only concatenate str (not "list") to str"

"float + int → ?"
print(decimal_number+number)
"= 125.1234"

"bool + bool → ?"
print(bool1 + bool2)
print(bool1 + bool3)
print(bool2 + bool4)
"= 1 - 2 - 0"

'''


"""
Cree un programa que le pida al usuario su nombre, apellido, y edad, 
y muestre si es un bebé, niño, preadolescente, adolescente, adulto joven, 
adulto, o adulto mayor.
"""

name = input("Please indicate your name:: ")
last_name = input("Please indicate your last name:: ")
age = int(input("Please indicate your age:: "))

if(age <= 5 ):
    print(f"Your name is {name} {last_name} and your age is {age}. You are a baby.")
elif(age <= 10):
    print(f"Your name is {name} {last_name} and your age is {age}. You are a child.")
elif(age<13):
    print(f"Your name is {name} {last_name} and your age is {age}. You are a preadolescent.")
elif(age<18):
    print(f"Your name is {name} {last_name} and your age is {age}. You are an adolescent.")
elif(age<25):
    print(f"Your name is {name} {last_name} and your age is {age}. You are a young adult.")
elif(age<60):
    print(f"Your name is {name} {last_name} and your age is {age}. You are an adult.")
else:
    print(f"Your name is {name} {last_name} and your age is {age}. You are an elderly adult.")
"""
Cree un programa con un numero secreto del 1 al 10. 
El programa no debe cerrarse hasta que el usuario adivine el numero.
Debe investigar cómo generar un número aleatorio distinto cada vez que se ejecute.
"""

import random
number = random.randint(1,10)
guessed = int(input("Please enter a number between 1 and 10: "))
while (number != guessed):
    guessed =int(input("Incorrect number. Please try again with a number between 1 and 10: "))
print(f"You have guessed the number {number}")

"""
Cree un programa que le pida tres números al usuario y muestre el mayor.
"""

largest_number = 0
first = int(input("Ingrese primer numero: "))
second = int(input("Ingrese segundo numero: "))
third = int(input("Ingrese tercer numero: "))
if(first>=second):
    mayor = first
elif(first<second):
    largest_number=second
    
    if(largest_number < third):
        largest_number = third
print(f"The largest number is {largest_number}")


"""
Dada n cantidad de notas de un estudiante, calcular:
Cuantas notas tiene aprobadas (mayor a 70).
Cuantas notas tiene desaprobadas (menor a 70).
El promedio de todas.
El promedio de las aprobadas.
El promedio de las desaprobadas.
"""

quantity = int (input("Indique la cantidad de notas a ingresar "))
counter = 1
total_grades= 0
number_failed= 0
failed_grades= 0
number_passed= 0
passed_grades= 0
average_failed = 0
average_passed = 0

while(counter <= quantity):
    grade = float(input("Ingrese la nota: "))
    total_grades = total_grades+grade
    average_total = total_grades/quantity
    counter = counter + 1
    if(grade<70):
        number_failed = number_failed+1
        failed_grades = failed_grades+grade
        average_failed = failed_grades/number_failed 
    elif(grade>=70):
        number_passed = number_passed+1
        passed_grades = passed_grades+grade
        average_passed = passed_grades/number_passed
print(f"Promedio total de notas es: {average_total}, \nEl promedio de notas aprobadas es {average_passed} cantidad : {number_passed}, \nEl prmedio de notas desaprobadas es: {average_failed} cantidad : {number_failed} ")     



