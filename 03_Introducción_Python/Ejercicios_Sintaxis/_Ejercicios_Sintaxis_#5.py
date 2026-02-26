
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



