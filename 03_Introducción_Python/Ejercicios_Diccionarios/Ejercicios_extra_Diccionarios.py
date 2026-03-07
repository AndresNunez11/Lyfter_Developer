"""
Dada una lista de ventas con la siguiente información:
date
customer_email
items
Y cada item teniendo la siguiente información:
name
upc
unit_price
Cree un diccionario que guarde el total de ventas de cada UPC.
"""


sales = [
	{
		'date': '27/02/23',
		'customer_email': 'joe@gmail.com',
		'items': [
			{
				'name': 'Lava Lamp',
				'upc': 'ITEM-453',
				'unit_price': 65.76,
			},
			{
				'name': 'Iron',
				'upc': 'ITEM-324',
				'unit_price': 32.45,
			},
			{
				'name': 'Basketball',
				'upc': 'ITEM-432',
				'unit_price': 12.54,
			},
		],
	},
	{
		'date': '27/02/23',
		'customer_email': 'david@gmail.com',
		'items': [
			{
				'name': 'Lava Lamp',
				'upc': 'ITEM-453',
				'unit_price': 65.76,
			},
			{
				'name': 'Key Holder',
				'upc': 'ITEM-23',
				'unit_price': 5.42,
			},
		],
	},
	{
		'date': '26/02/23',
		'customer_email': 'amanda@gmail.com',
		'items': [
			{
				'name': 'Key Holder',
				'upc': 'ITEM-23',
				'unit_price': 3.42,
			},
			{
				'name': 'Basketball',
				'upc': 'ITEM-432',
				'unit_price': 17.54,
			},
		],
	},
]
new_dictionary = {}
new_key = ''
new_value = 0

for sale in sales:
    for item in sale['items']:
        for key, value in item.items():
            if key == 'upc':
                new_key = value
            if key == 'unit_price':
                new_value = new_dictionary.get(new_key, 0) + value
                new_dictionary[new_key] = new_value            
print(new_dictionary)

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