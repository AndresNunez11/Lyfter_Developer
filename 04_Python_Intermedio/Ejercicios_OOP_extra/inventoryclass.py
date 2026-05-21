class Inventory:
    
    def __init__(self):
        self.product_list = []
    
    def add_product(self, product):
        self.product_list.append(product)

    def show_products(self):
        try:
            for product in self.product_list:
                print(f'Descripcion: {product.name}\n Precio: {product.price}\n Cantidad: {product.quantity}')
        except Exception as e:
            print(f'Error al mostrar productos. Error: {e} ')
    
    def calculate_total_value_of_inventory(self):
        try:
            result = 0
            for product in self.product_list:
                result = result + (product.price * product.quantity)
            return result
        except Exception as e:
            print(f'Error al calcular el valor total del inventario. Error: {e}')



    
