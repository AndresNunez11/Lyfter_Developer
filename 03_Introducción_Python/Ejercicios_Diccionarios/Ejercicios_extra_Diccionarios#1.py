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

