
"""
Cree un programa que le pida al usuario 10 números, 
y al final le muestre todos los números que ingresó, 
seguido del numero ingresado más alto.
"""


my_list = []
counter = 0
largest_number = 0
while (counter < 10):
    number = int(input("Ingrese un numero: "))
    if(largest_number < number):
        largest_number = number
    my_list.append(number)
    counter+=1
print(f'La lista de nuemros ingresados es: {my_list} y el numero mayor es: {largest_number}')











