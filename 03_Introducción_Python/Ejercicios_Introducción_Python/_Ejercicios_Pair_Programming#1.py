
"""
Dadas las horas trabajadas de una persona y su tarifa por hora, calcular y mostrar su salario.
"""
horas_trabajadas = 0
tarifa_hora = 0
salario = 0
horas_trabajadas= int (input("Ingrese horas trabajadas"))
tarifa_hora = int(input("Ingrese la tarifa por hora"))
salario = horas_trabajadas * tarifa_hora
print(f"El salrio es de: {salario}")
