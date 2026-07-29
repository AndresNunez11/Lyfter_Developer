import actionclass

PATH_CSV_FILE = '04_Python_Intermedio\Estructuras de Datos\Exercises.json'

#Funcion principal del sistema 
def main():
    try:        
        menu = actionclass.Menu_Actions(PATH_CSV_FILE)
        menu.read_json_file()       
        while True:
            try:
                print(f"******Menu Principal******")
                menu.show_menu()
                option = int(input(f'Digite el número de la opción a elegir: \n'))
                match option:
                    case 0:
                        print(f'Fin de la aplicacion')
                        break
                    case 1: 
                        print(f'{menu.list_exercise[1]}')                        
                        menu.show_linked_list()
                        input('Presione [Enter] para continuar \n')
                    case 2:
                        print(f'{menu.list_exercise[2]}') 
                        menu.show_queue()                  
                        input('Presione [Enter] para continuar')
                    case 3: 
                        print(f'{menu.list_exercise[3]}')   
                        menu.show_stack()                   
                        input('Presione [Enter] para continuar')
                    case 4: 
                        print(f'{menu.list_exercise[4]}')
                        menu.show_DobleEndedQueue()
                        input('Presione [Enter] para continuar')
                    case 5: 
                        print(f'{menu.list_exercise[5]}')
                        menu.show_BinaryTree()
                        input('Presione [Enter] para continuar')
            except IndexError as e:
                print(f'La opción elegida no esta dentro de las disponibles. Error: {e}')
            except ValueError as e:
                print(e)
                input("Presione [Enter] para continuar...")
                print(f'El valor ingresado no es correcto. Se reinicia la aplicación. {e}')
            except Exception as e:
                print(f'Error en el menu principal. Error: {e}')
    except Exception as e:
        print(f'Existe un error al iniciar la aplicacion {e}')
        

#Inicio del Sistema
if __name__ == "__main__":
    main()

    