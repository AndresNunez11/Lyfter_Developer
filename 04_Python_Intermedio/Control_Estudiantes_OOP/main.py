import menu

# Variables Globales
#Utilizar la variable global en la mayuscula cuando es inmutable -- 
PATH_JSON_FILE = '04_Python_Intermedio/Control_Estudiantes_OOP/Estudiantes.json' 
PATH_CSV_FILE = '04_Python_Intermedio/Control_Estudiantes_OOP/Estudiantes.csv' 

#Funcion principal del sistema 
def main(PATH_CSV_FILE):
    try:
        menu.menu(PATH_CSV_FILE)
    except Exception as e:
        print(f'Existe un error al iniciar la aplicacion {e}')

#Inicio del Sistema
if __name__ == "__main__":
    main(PATH_CSV_FILE)
    


