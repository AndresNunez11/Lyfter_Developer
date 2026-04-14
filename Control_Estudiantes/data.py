import json
import csv
import os

#Variables Globales inmutables

HEATHERS_FILE = ["name","section","spanish_grade","english_grade","social_grade","science_grade"]


# Leer archivo de CSV con informacion de estudiantes, si no existe crea el archivo

def read_csv_file(std_list,path_csv_file):
    student_list= std_list
    try:
        if not os.path.exists(path_csv_file):
            print("El archivo no existe. Se creará uno nuevo.")
            # Crear archivo con encabezados (ajústalos a tu estructura)
            with open(path_csv_file, 'w', newline="", encoding='utf-8') as file:
                fieldnames = HEATHERS_FILE
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
            return student_list
        else:
            with open(path_csv_file,'r', newline="", encoding='utf-8')as file:
                reader= csv.DictReader(file)
                
                for row in reader:
                    student_list.append(row)
            return student_list
    except Exception as e:
        print(f'Error al intentar leer archivo csv. Error: {e}')




# Leer archivo de Json con informacion de estudiantes, si no existe crea el archivo
# def read_json_file(path_json_file):
#     student_list = []
#     try:
#         with open(path_json_file, "r", encoding="utf-8" ) as file:
#             data = json.load(file)
#             if (data, list):
#                 student_list = data
#                 return student_list
#             else:
#                 return student_list  
#     except FileNotFoundError:
#         print(f"Archivo no encontrado, se creará uno nuevo {path_json_file}")
#         return student_list
#     except json.JSONDecodeError:
#         print("Archivo JSON corrupto, se inicia con lista vacía")
#         return student_list
#     except Exception as e:
#         print(f'Error al leer archivo JSON {e}')

# Funcion para guardar datos en csv

def save_new_student(student_list, path_csv_file):
    try:
        file_exists = os.path.exists(path_csv_file)
        with open(path_csv_file, 'a', newline='', encoding='utf-8') as file:
            #Tomamos las llaves del primer diccionario como encabezados
            fieldnames = student_list[0].keys()
            
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            # Escribir encabezados solo si el archivo no existe
            if not file_exists:
                print(f'Se creara un nuevo archivo csv para almacenar la informacion de los estudiantes.')
                writer.writeheader()

            # Escribir todos los estudiantes
            writer.writerows(student_list)
    except Exception as e:
        print(f'Error al guardar nuevo estudiante {e}')





# Guardar datos en json -- simula BD
#  Metodo dump
# Convierte estructuras de Python como:
# diccionarios (dict)
# listas (list)
# strings, números, booleanos
# en formato JSON
# y los escribe en un archivo 


# def save_new_student(student_list, path_json_file):
#     try:
#         with open(path_json_file, "w", encoding="utf-8" ) as file:
#             json.dump(student_list, file, indent=4, ensure_ascii=False)
#     except Exception as e:
#         print(f'Error al guardar nuevo estudiante {e}')

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
                if not any(reader):
                    print("El CSV está vacío (sin datos)")
                else:
                    for row in reader:
                        i+=1
                        print(f'Linea #{i}')
                        print(f"Estudiante: {row}")
        else:
            print('El archivo no ha sido exportado anteriormente')
    except Exception as e:
        print(f'Error al leer archivo {e}')

