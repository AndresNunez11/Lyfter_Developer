
'''Usando metodo Apppend'''
'''
new_department = ''
new_name = ''
new_email = ''
for employee in employees:
    for key, value in employee.items():
        if key == 'name':
            new_name = value
            print(new_name)
        if key == 'email':
            new_email = value
        if key == 'department':
            new_department = value
    new_employee = {'name': new_name, 'email': new_email}
    if new_department in department:
        department[new_department].append(new_employee)
    else:
        department[new_department] = [new_employee] 
print(department)
'''

"""
Dada una lista de productos vendidos, 
donde cada uno tiene categoría y precio, 
cree un diccionario que acumule el total por categoría.
"""

products = [
    {"name": "Monitor", "category": "Electrónica", "price": 200},
    {"name": "Teclado", "category": "Electrónica", "price": 50},
    {"name": "Silla", "category": "Muebles", "price": 120},
    {"name": "Mesa", "category": "Muebles", "price": 180},
    {"name": "Mouse", "category": "Electrónica", "price": 25},
]

category_by_price = {}

for product in products:
    category = product["category"]
    price = product["price"]
    total_price = category_by_price.get(category, 0) + price
    category_by_price[category] = total_price
print(category_by_price)