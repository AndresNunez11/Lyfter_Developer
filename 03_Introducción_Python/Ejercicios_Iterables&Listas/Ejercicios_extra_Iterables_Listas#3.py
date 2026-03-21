
"""
Cree un programa que muestre el valor más pequeño de una lista sin usar min().
"""

my_list=[9,4,7,1,5]
minor_number=my_list[0]
counter = 0

for number in my_list:
    if(minor_number > number):
        minor_number = number
print(f'El menor valor es: {minor_number}')

