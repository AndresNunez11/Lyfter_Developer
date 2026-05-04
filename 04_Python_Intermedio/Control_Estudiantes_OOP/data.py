import json
import csv
import os

#Variables Globales inmutables

HEATHERS_FILE = ["name","section","spanish_grade","english_grade","social_grade","science_grade"]


# Leer archivo de CSV con informacion de estudiantes, si no existe crea el archivo

def read_csv_file(path_csv_file):
    student_list= []
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
        data_dict = [student.to_dict() for student in data] # Los datos de la lista que son objetos los transforma en un diccionario
        '''# Otra forma es manual
        data_dict = []
            for student in data:
                data_dict.append({
                    "name": student.name,
                    "section": student.section,
                    "average": student.average
                })
        '''
        with open(csv_path_file, 'w', newline="", encoding='utf-8')as file:
            writer= csv.DictWriter(file, myheaders)
            writer.writeheader()
            writer.writerows(data_dict)
            print('Archivo exportado a CSV')
    except Exception as e:
        print(f'Error al exportar informacion a formato CSV. Error : {e}')


#Importar datos de csv
def csv_import(csv_path_file):
    try:
        i=0
        csv_list = []
        if(os.path.exists(csv_path_file)):
            with open(csv_path_file,'r', newline="", encoding='utf-8')as file:
                reader = list(csv.DictReader(file))
                if not (reader): #No utilizar any para evitar consumir el primer dato --if not any--
                    print("El CSV está vacío (sin datos)")
                else:
                    for i, row in enumerate(reader):
                        # print(f'Linea #{i}')
                        # print(f"Estudiante: {row}")
                        csv_list.append(row)
            print(f'Archivo csv leido correctamente')
        else:
            print('El archivo no ha sido exportado anteriormente')
        return csv_list
    except Exception as e:
        print(f'Error al leer archivo {e}')

