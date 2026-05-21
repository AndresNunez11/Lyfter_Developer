
"""
Dado el nombre y apellido de un empleado, y el dominio .com de una empresa, 
genere su email usando el formato <nombre>.<apellido>@<dominio_de_empresa>.com.
"""

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
dominio = input("Ingrese el dominio de su correo: ")

correo = f"{nombre}.{apellido}@{dominio}.com"
print(f"Su correo es: {correo} ")