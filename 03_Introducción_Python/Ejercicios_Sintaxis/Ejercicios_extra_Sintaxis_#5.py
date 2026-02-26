


"""
Cree un diagrama de flujo que pida 3 números al usuario. 
Si uno de esos números es 30, o si los 3 sumados dan 30, 
mostrar Correcto. Sino, mostrar incorrecto.
Ejemplos:
23, 30, 768 → Correcto (hay un 30)
10, 15, 5 → Correcto (10 + 15 + 5 = 30)
35, 56, 2 → Incorrecto (no hay ningún 30, y la suma de ellos tampoco da 30)
"""


firts = int(input('Ingrese primer numero: '))
second = int(input('Ingrese segundo numero: '))
third= int(input('Ingrese tercer numero: '))
if(firts == 30 or second ==30 or third==30):
    print(f'Correcto, hay un 30 entre los 3 numeros')
elif(firts + second + third == 30):
    print(f'Correcto, la suma de los 3 numeros es 30')
else:
    print(f'Incorrecto, no hay ningún 30, y la suma de ellos tampoco da 30')


