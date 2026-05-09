import rectangleclass
import dogclass
import catclass
import animalclass
import productclass
import inventoryclass

#Funcion principal del sistema 
def main():
    try:
        while True:
            try:
                print(f"******Menu Principal******")
                print(f'Opciones:\n 0-Salir\n 1- Ejercicio Clase Rectangulo \n 2- Ejercicio Clase Aninal \n 3- Ejercicio Clase Producto \n')
                option = int(input(f'Digite el número de la opción a elegir: \n'))
                match option:
                    case 0:
                        print(f'Fin de la aplicacion')
                        break
                    case 1: 
                        print(f'Ejercicio 1: Area y Perimetro del rectangulo')
                        my_rectangule = rectangleclass.Rectangule()
                        print(f' El area del rectangulo es: {my_rectangule.area}, y el perimetro del rectangulo es: {my_rectangule.perimeter}.')
                    case 2:
                        print(f'Ejercicio 2: Animal y dos clases hijas Dog y Cat')
                        animal = animalclass.Animal("Animal")
                        perro = dogclass.Dog("Firulais")
                        gato = catclass.Cat("Michi")
                        print(f"{animal.nombre}: {animal.speak()}")
                        print(f"{perro.nombre}: {perro.speak()}")
                        print(f"{gato.nombre}: {gato.speak()}")                        
                    case 3: 
                        print(f'Ejercicio 3: Clase Producto e Inventario')
                        product1 = productclass.Product("Mouse", 5000, 3)
                        product2 = productclass.Product("Teclado", 8000, 2)                       
                        inventory = inventoryclass.Inventory()
                        inventory.add_product(product1)
                        inventory.add_product(product2)
                        inventory.show_products()
                        print(f'El valor total del inventario es: {inventory.calculate_total_value_of_inventory()}')
            except IndexError as e:
                print(f'La opción elegida no esta dentro de las disponibles. Error: {e}')
            except ValueError as e:
                print(f'El valor ingresado no es un numero entero {e}')
            except Exception as e:
                print(f'Error en el menu principal. Error: {e}')
    except Exception as e:
        print(f'Existe un error al iniciar la aplicacion {e}')

#Inicio del Sistema
if __name__ == "__main__":
    main()