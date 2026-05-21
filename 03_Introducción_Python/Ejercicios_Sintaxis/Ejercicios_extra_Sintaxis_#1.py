
"""
Pasa los Ejercicios de Pseudocodigo previamente creados a código:
Cree un pseudocódigo que le pida un precio de producto al usuario, 
calcule su descuento y muestre el precio final tomando en cuenta que:
Si el precio es menor a 100, el descuento es del 2%.
Si el precio es mayor o igual a 100, el descuento es del 10%.
Ejemplos:
120 → 108
40 → 39.2
"""


price = float(input('Ingrese el precio del Producto: '))
if(price < 100):
    final_price = price - (price * 0.02 )
elif(price >= 100):
    final_price = price - (price * 0.10)
print(f'El precio final es de {final_price}')




