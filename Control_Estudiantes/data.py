import json
import csv
import os

# Leer archivo de Json con informacion de estudiantes, si no existe crea el archivo
def read_json_file(path_json_file):
    student_list = []
    try:
        with open(path_json_file, "r", encoding="utf-8" ) as file:
            data = json.load(file)
            if (data, list):
                student_list = data
                return student_list
            else:
                return student_list  
    except FileNotFoundError:
        print(f"Archivo no encontrado, se creará uno nuevo {path_json_file}")
        return student_list
    except json.JSONDecodeError:
        print("Archivo JSON corrupto, se inicia con lista vacía")
        return student_list
    except Exception as e:
        print(f'Error al leer archivo JSON {e}')

# Guardar datos en json -- simula BD
def save_new_student(student_list, path_json_file):
    try:
        with open(path_json_file, "w", encoding="utf-8" ) as file:
            json.dump(student_list, file, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f'Error al guardar nuevo estudiante {e}')

# Exportar los datos a formato csv
def csv_export(csv_path_file, data, myheaders):
    try:
        with open(csv_path_file, 'w', newline="", encoding='utf-8')as file:
            writer= csv.DictWriter(file, myheaders)
            writer.writeheader()
            writer.writerows(data)
            print('Archivo exportado a CSV')
    except Exception as e:
        print(f'Error al exportar informacion a formato CSV. Error : {e}')


#Importar datos de csv
def csv_import(csv_path_file):
    try:
        i=0
        if(os.path.exists(csv_path_file)):
            with open(csv_path_file,'r', newline="", encoding='utf-8')as file:
                reader= csv.DictReader(file)
                for row in reader:
                    i+=1
                    print(f'Linea #{i}')
                    print(f"Estudiante: {row}")
        else:
            print('El archivo no ha sido exportado anteriormente')
    except Exception as e:
        print(f'Error al leer archivo {e}')

