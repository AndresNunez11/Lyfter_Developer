import actions

#Opciones del menu, esta en el codigo pero podria trarse de un json o BD
#Utilizar la variable global en la mayuscula cuando es inmutable -- 
MENU_LIST= ["0- Salir",
"1- Ingresar Estudiante", "2- Informacion de Estudiantes", 
"3- Top 3 Estudiantes Mejor Promedio", "4- Promedio total", 
"5- Exportar datos a CSV", "6- Importar datos desde CSV", 
"7-Eliminar un estudiante de la lista", "8-Lista de Estudiantes Reprobados"]

# Funcion principal para desplegar el menu
def menu(path_csv_file):
    try: 
        new_std_list = []
        #new_std_list = actions.read_json_file(path)
        while True:
            try:
                print(f"******Menu Principal******")
                print(f'Opciones:\n')
                for item in MENU_LIST:
                    print(f'{item}')
                option = int(input(f'Digite el número de la opción a elegir: \n'))
                print(f'La opción elegida es {MENU_LIST[option]}')
                match option:
                    case 0:
                        print(f'Fin de la aplicación')
                        break
                    case 1:
                        print(f'Ingresar datos del estudiante:\n')
                        new_std_list = actions.new_student(new_std_list)
                        #actions.new_student(new_std_list, path)
                    case 2:
                        print('Se muestra la informacion de todos los estudiantes: \n')
                        actions.show_all_students(new_std_list) #path_csv_file
                    case 3:
                        print('Top 3 de estudiantes con promedio de notas mas alto: \n')
                        actions.top_3_average(new_std_list) #path_csv_file
                    case 4: 
                        print('El promedio total de todos los estudiantes es :\n')
                        actions.total_average(new_std_list) #path_csv_file
                    case 5:
                        print('Generar archivo y exportar a formato CSV :\n')
                        actions.ftn_csv_export(new_std_list,path_csv_file)
                    case 6:
                        print('Validar archivo e importar de formato CSV. Los datos del archivo son: \n')
                        new_std_list = actions.ftn_csv_import(new_std_list, path_csv_file)
                    case 7: 
                        print('Proceso para eliminar un estudiante de la lista: \n')
                        new_std_list = actions.ftn_delete_student(new_std_list) #path_csv_file
                    case 8:
                        print("Se muestra la informacion de los estudiantes reprobados")
                        actions.ftn_failed_students(new_std_list) #path_csv_file
            except IndexError as error:
                print(f'La opción elegida no esta dentro de las disponibles. Error: {error}')
            except ValueError as e:
                print(f'El valor ingresado no es un numero entero {e}')
            except Exception as e:
                print(f'Error al desplegar el menu {e}')
    except Exception as e:
        print(f'Error al iniciar el menu, no lee archivo json. Error: {e}')