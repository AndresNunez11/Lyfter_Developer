

"""
Agrupar empleados por departamento
Dada una lista de empleados donde cada uno tiene nombre, 
correo y departamento, 
cree un diccionario que agrupe los empleados por su departamento
"""

employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"},
]
department = {}
new_employee={}
for employee in employees:
    dept = employee["department"]
    new_employee = {"name": employee["name"], "email": employee["email"]}

    current_list = department.get(dept, [])
    department[dept] = current_list + [new_employee]
print(department)
