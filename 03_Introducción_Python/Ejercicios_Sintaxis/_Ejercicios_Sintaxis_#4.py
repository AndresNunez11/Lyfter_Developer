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

