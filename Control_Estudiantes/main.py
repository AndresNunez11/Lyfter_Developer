import menu

# Variables Globales
path_json_file = 'Control_Estudiantes/Estudiantes.json' 

#Funcion principal del sistema 
def main(path_json_file):
    try:
        menu.menu(path_json_file)
    except Exception as e:
        print(f'Existe un error al iniciar la aplicacion {e}')

#Inicio del Sistema
if __name__ == "__main__":
    main(path_json_file)