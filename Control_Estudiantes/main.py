import menu

# Variables Globales
#Utilizar la variable global en la mayuscula cuando es inmutable -- 
PATH_JSON_FILE = 'Control_Estudiantes/Estudiantes.json' 
PATH_CSV_FILE = 'Control_Estudiantes/Estudiantes.csv' 

#Funcion principal del sistema 
def main(PATH_CSV_FILE):
    try:
        menu.menu(PATH_CSV_FILE)
    except Exception as e:
        print(f'Existe un error al iniciar la aplicacion {e}')

#Inicio del Sistema
if __name__ == "__main__":
    main(PATH_CSV_FILE)

