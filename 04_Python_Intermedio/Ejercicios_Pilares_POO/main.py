import actionclass

PATH_CSV_FILE = '04_Python_Intermedio/Ejercicios_Pilares_POO/Exercises.json' 

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
                        menu.balance = menu.bankacount(0)
                        input('[Enter] para continuar')
                    case 2:
                        print(f'{menu.list_exercise[2]}')
                        min_amount = 50
                        amount= int(input(f'Digite el monto a retirar\n'))
                        new_balance =  menu.saving_account(min_amount, amount, menu.balance)
                        # print(new_balance)
                        menu.balance = new_balance 
                        # print(menu.balance)
                        input('[Enter] para continuar')
                    case 3: 
                        print(f'{menu.list_exercise[3]}')
                        menu.calculate_shapes()
                        input('[Enter] para continuar')
                    case 4: 
                        print(f'{menu.list_exercise[4]}')
                        menu.Inheritance()
                        input('[Enter] para continuar')
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