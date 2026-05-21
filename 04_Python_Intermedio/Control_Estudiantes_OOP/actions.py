import data
import studentclass, nameclass, sectionclass, gradeclass

#variables globales
#No utilizar variables globales si van a estar definiendose en diferentes funciones
#student_list= []

HEATHERS_FILE = ['name', 'section', 'spanish_grade', 'english_grade', 'social_grade', 'science_grade', 'average']

#Clase para que el nombre no incluya un numero
class nameTypeError(Exception):
    def __init__(self,name):
        super().__init__(f'\n El nombre no puede ser o incluir un número')
    
#Clase para que el nombre no puede estar vacio
class emptyTypeError(Exception):
    def __init__(self,name):
        super().__init__(f'\n El nombre no puede esta vacio')

#Clase para validar que el nombre este compuesto por tres palabras
class completeTypeError(Exception):
    def __init__(self,name):
        super().__init__(f'\n Debe ingresar al menos nombre y dos apellido')

#Clase para que el formato de la seccion
class formatTypeError(Exception):
    def __init__(self,name):
        super().__init__(f'\n El formato de la seccion es incorrecto, debe ser numero-numero-letra')

# Exception Negative Number
def no_negative_number(enter_number):
    if enter_number < 0:
        raise ValueError("El número no puede ser menor que cero")
    return enter_number

#Validar que la nota ingresada este entre 0 y 100
def grade_number(enter_number):
    if enter_number < 0 or enter_number > 100 :
        raise ValueError("El número no puede ser menor que cero o mayor a 100")
    return enter_number

# Excepcion para no ingresar espacion en el nombre o tipo
def no_spaces_text(enter_text):
    if " " in enter_text:
        raise ValueError("El texto no debe contener espacios en blanco")
    return enter_text

# Excepcion para no ingresar un estudiante que ya este en la lista
def no_duplicate_student(enter_text, std_list):
    if not std_list:
        print(f'Lista principal vacia, se agrega primer Estudiante')
        return enter_text
    else:
        for student in std_list:
            if enter_text == student.name:
                raise ValueError("El estudiante ya fue agregado a la lista de estudiantes")
        return enter_text
    

#Excepcion para validar el nombre no sea un numero
def validate_name(enter_text):
    for char in enter_text:
        if(char.isdigit()):
            raise nameTypeError(enter_text)
    return enter_text

#Excepcion para validar el nombre no este vacio
def validate_empty_name(enter_text):
    if enter_text.strip() == "":
        raise emptyTypeError(enter_text)
    return enter_text

#Excepcion para validar que se agregue nombre completo 
def validate_complete_name(enter_text):
    complete_name = enter_text.strip().split()
    if len(complete_name)<3:
        raise completeTypeError(enter_text)
    return enter_text

#Excepcio para validar el formato de la seccion
def validate_section_format(enter_text):
    if(len(enter_text)!=3):
        raise formatTypeError(enter_text)
    if not enter_text[:2].isdigit():
        raise formatTypeError(enter_text)
    if not enter_text[2].isalpha():
        raise formatTypeError(enter_text)   
    return enter_text    


# Funcion para leer los datos desde Json, utilizando modulo de data
# def read_json_file(path_json_file):
#     student_list = data.read_json_file(path_json_file)
#     return student_list

# Funcion para leer los datos desde csv, utilizando modulo de data
def read_csv_file(path_csv_file):
    student_list = data.read_csv_file(path_csv_file)
    return student_list

# Funcion para agregar a un nuevo estudiante a la base de estudiantes
def new_student(new_std_list):
    new_student_list = new_std_list or [] 
    while True:
        try:
            name_obj = nameclass.Name()
            name = name_obj.name
            no_duplicate_student(validate_complete_name(validate_empty_name(validate_name(name))),new_student_list)
            section_obj = sectionclass.Section()
            section = section_obj.section
            validate_section_format(section)
            print(f'Para la materia de español ingrese la nota')
            spanish_grade_obj = gradeclass.grade()
            spanish_grade = spanish_grade_obj.grade
            grade_number(int(spanish_grade))
            print(f'Para la materia de ingles ingrese la nota')
            english_grade_obj = gradeclass.grade()
            english_grade = english_grade_obj.grade
            grade_number(int(english_grade))
            print(f'Para la materia de estudios sociales ingrese la nota')
            social_grade_obj = gradeclass.grade()
            social_grade = social_grade_obj.grade
            grade_number(int(social_grade))
            print(f'Para la materia de ciencia ingrese la nota')
            science_grade_obj = gradeclass.grade()   
            science_grade = science_grade_obj.grade
            grade_number(int(science_grade))

            student  =  studentclass.Student(name,section, spanish_grade, english_grade, social_grade, science_grade)
            # new_student = {
            #     "name": student.name,
            #     "section":student.section,
            #     "spanish_grade": student.spanish_grade,
            #     "english_grade":student.english_grade,
            #     "social_grade":student.social_grade,
            #     "science_grade":student.science_grade
            #     }
            new_student_list.append(student)
            print(f'Informacion del estudiante agregada a la lista')
            # print(new_student_list)
            # data.save_new_student(new_student_list,path_csv_file)
            student = ""
            desicion = input(f'Para agregar otro estudiante digite Y o para salir digite N -> ').upper()
            if desicion != 'Y':
                break
        except nameTypeError as error:
            print(f'Error: {error}\nDato ingresado no es correcto. Intente nuevamente.')
            desicion = input(f'Para continuar con el ingreso de estudiantes digite Y o para salir digite N -> ').upper()
            if desicion != 'Y':
                break
        except emptyTypeError as error:
            print(f'Error: {error}\nDato ingresado no es correcto. Intente nuevamente.')
            desicion = input(f'Para continuar con el ingreso de estudiantes digite Y o para salir digite N -> ').upper()
            if desicion != 'Y':
                break
        except completeTypeError as error:
            print(f'Error: {error}\nDato ingresado no es correcto. Intente nuevamente.')
            desicion = input(f'Para continuar con el ingreso de estudiantes digite Y o para salir digite N -> ').upper()
            if desicion != 'Y':
                break
        except formatTypeError as error:
            print(f'Error: {error}\nDato ingresado no es correcto. Intente nuevamente.')
            desicion = input(f'Para continuar con el ingreso de estudiantes digite Y o para salir digite N -> ').upper()
            if desicion != 'Y':
                break
        except  ValueError as error:
            print(f'Error: {error}\nDato ingresado no es correcto. Intente nuevamente.')
            desicion = input(f'Para continuar con el ingreso de estudiantes digite Y o para salir digite N -> ').upper()
            if desicion != 'Y':
                break
        except Exception as e:
            print(f'Existe un error al ingresar el nuevo estudiante. Error: {e}')
    return new_student_list

# Funcion para mostrar la informacion de los estudiantes registrados en la base de estudiantes
def show_all_students(student_list):
    try:
        new_std_list = student_list
        # new_std_list = read_csv_file(path_csv_file)
        i=0
        for student in new_std_list:
            i+=1
            print(f'Estudiante # {i}')
            print(f'Nombre: {student.name} \nSección: {student.section} \n Nota Español: {student.spanish_grade} \n Nota Ingles: {student.english_grade} \n Nota Estudios Sociales: {student.social_grade} \n Nota Ciencias: {student.science_grade}')

    except Exception as e:
        print(f'Error al mostrar informacion d elos estudiantes. Error: {e}')

# Funcion para obtener top 3 de mejor promedio
'''
Se puede utilizar una funcion que me ordene la lista sorted(iterable, key=funcion, reverse=False)
iterable → lista, tupla, etc.
key → cómo se debe ordenar
reverse → si el orden es descendente (reverse=True 90 82 75 // reverse False 75 82 90)
top3 = sorted(new_std_list, key=lambda s: s["average"], reverse=True)[:3]
'''
"""
codigo para ordenar la lista
            if(len(sort_list)==0):
                sort_list.append(new_student)
            else:
                for index,item in enumerate(sort_list):
                    if(item['average']<grade_average):
                        sort_list.insert(index, new_student) 
                        break
"""  
def top_3_average(student_list):
    try:
        # student_list.sort(key=lambda x: x.average, reverse=True)  # No generar un retorno por eso no funciona
        sort_list = sorted(student_list, key=lambda x: x.average, reverse=True)  # funcion que le indica a la lista como debe de ordenarse, en este caso por el promedio
        top_3 = sort_list[:3]
        for student in top_3:
            print(f'Nombre Estudiante: {student.name}')
            print(f'Sección Estudiante: {student.section}')
            print(f'Promedio Estudiante: {student.average}\n')
    except Exception as e:
        print(f'Error al obtener el top 3 en promedio de notas. Error: {e} ')

# Funcion para calcular el promedio total de todos los estudantes (std = student  // stds students)
def total_average(student_list):
    try:
        grade_average = 0
        for student in student_list:
            grade_average = grade_average + student.average
        index = len(student_list)
        final_average = grade_average/index
        print(f"Total de estudiantes: {index}\n Promedio ponderado de notas : {final_average}" )
    except Exception as e:
        print(f'Error al obtener el  promedio total de notas de todos los estudiantes. Error: {e} ')

# Funcion para exportar los datos a CSV - Validar si existe el archivo y exportar  la lista actual
def ftn_csv_export(student_list,path_csv_file):
    try:
        headers=HEATHERS_FILE
        std_data = read_csv_file(path_csv_file) 
        # if not std_data:
        #     headers = HEATHERS_FILE
        data.csv_export(path_csv_file,student_list, headers)
    except Exception as e:
        print(f'Error en funcion para exportar datos a CSV. Error: {e}')

# Funcion para importar los datos a CSV
def ftn_csv_import(new_std_list, path_csv_file):
    try:
        i=0
        csv_list = data.csv_import(path_csv_file)  
        # print(f'Imprime la lista desde l funcion importar {new_std_list}')
        # print(f'La lista es {csv_list}')
        if not csv_list:
            print("No se agregan datos al sistema, se mantiene la lista original.")
            for student in new_std_list:
                i+=1
                print(f'Estudiante{i}: {student.name} ')
            return new_std_list
        else: 
            print(f'Total de estudiantes en csv {len(csv_list)}')
            for item in csv_list:
                i+=1
                print(f'El estudiante importado del CSV es {i} - {item['name']}')
                # while True:
                try:
                    name= no_duplicate_student(validate_complete_name(validate_empty_name(validate_name(item['name']))),new_std_list)
                    section = validate_section_format(item['section'])
                    spanish_grade = grade_number(int(item['spanish_grade']))
                    english_grade = grade_number(int(item['english_grade']))
                    social_grade = grade_number(int(item['social_grade']))
                    science_grade = grade_number(int(item['science_grade']))
                    student_obj = studentclass.Student(name, section, spanish_grade, english_grade, social_grade, science_grade)
                    
                    new_std_list.append(student_obj)
                    # break
                except nameTypeError as error:
                    print(f'Error: {error}\nDato ingresado no es correcto, no se puede agregar. Se continua al siguiente registro.')
                    # break
                except emptyTypeError as error:
                    print(f'Error: {error}\nDato ingresado no es correcto, no se puede agregar. Se continua al siguiente registro.')
                    # break
                except completeTypeError as error:
                    print(f'Error: {error}\nDato ingresado no es correcto, no se puede agregar. Se continua al siguiente registro.')
                    # break
                except formatTypeError as error:
                    print(f'Error: {error}\nDato ingresado no es correcto, no se puede agregar. Se continua al siguiente registro.')
                    # break
                except  ValueError as error:
                    print(f'Error: {error}\nDato ingresado no es correcto, no se puede agregar. Se continua al siguiente registro.')
                    # break    
            print(f'Se completa proceso de importar CSV Se actualiza la lista de estudiantes.')
            show_all_students(new_std_list)            
            return new_std_list
    except Exception as e:
        print(f'Error en funcion para importar datos a CSV. Error: {e}')

#Funcion para eliminar un estudiante de la lista
def ftn_delete_student(student_list):
    try:
        # std_list = read_csv_file(path_csv_file) or []
        std_list =  student_list
        student_name= input('Digete el nombre del estudiante: \n')
        student_section = input('Digite la seccion del estudiante: \n')
        exist = 'Y'
        for index, student in enumerate(std_list):
            if(student.name==student_name and student.section == student_section):
                desicion= input('Digite Y para eliminar, o N para salir: \n').upper()
                if(desicion == 'Y'):
                    delete_student = std_list.pop(index)
                    print(f'El estudiante {delete_student.name} se elimino de la lista')
                else:
                    print('No se elimina ningun registro')
                exist = 'Y'
                break
            else:
                exist = 'N'
        #print(exist)
        if(exist== "N"):
            print(f'El estudiante {student_name} seccion {student_section}, no existe en los registros. Favor validar.')
        else:
            print('Se actualiza informacion en BD')
            return std_list
            # data.save_new_student(std_list,path_csv_file)
        #print(f'{std_list}')
    except Exception as e:
        print(f'Error al tratar de eliminar estudiante de la lista. Error: {e} ')

# funcion para listar los estudiantes reprobados
def ftn_failed_students(student_list):
    try:
        # std_list = read_csv_file(path_csv_file) or []
        std_list = student_list
        failed_student_list = []
        quantiy = 0
        for student in std_list:
            #print(student)
            if int(student.spanish_grade) < 70 or int(student.english_grade)<70 or int(student.social_grade)<70 or int(student.science_grade)<70:
                quantiy+= 1
                failed_student_list.append(student)
        print(f'La cantidad de estudiantes reprobados es {quantiy}\n')
        show_all_students(failed_student_list)    
    except Exception as e:
        print(f'Error al mostrar a los estudiantes reprobados. Error: {e}')
            
# Funcion para importar los datos a CSV y validar los datos contra la lita en memoria
def ftn_csv_import_memoria(new_std_list, path_csv_file):
    try:
        i=0
        csv_list = data.csv_import(path_csv_file)  
        # print(f'Imprime la lista desde l funcion importar {new_std_list}')
        # print(f'La lista es {csv_list}')
        if not csv_list:
            print("No se agregan datos al sistema, se mantiene la lista original.")
            for student in new_std_list:
                print(f'Estudiante: {student} ')
            return new_std_list
        else: 
            print(f'Total de estudiantes en csv {len(csv_list)}')
            for item in csv_list:
                i+=1
                print(f'El estudiante importado del CSV es {i} - {item['name']}')
                # while True:
                try:
                    name= no_duplicate_student(validate_complete_name(validate_empty_name(validate_name(item['name']))),new_std_list)
                    student_name = name
                    student_section = validate_section_format(item['section'])
                    spanish_grade = grade_number(int(item['spanish_grade']))
                    english_grade = grade_number(int(item['english_grade']))
                    social_grade = grade_number(int(item['social_grade']))
                    science_grade = grade_number(int(item['science_grade']))
                    new_student = {
                        "name": student_name,
                        "section":student_section,
                        "spanish_grade": spanish_grade,
                        "english_grade":english_grade,
                        "social_grade":social_grade,
                        "science_grade":science_grade
                        }
                    new_std_list.append(new_student)
                    # break
                except nameTypeError as error:
                    print(f'Error: {error}\nDato ingresado no es correcto, no se puede agregar. Se continua al siguiente registro.')
                    # break
                except emptyTypeError as error:
                    print(f'Error: {error}\nDato ingresado no es correcto, no se puede agregar. Se continua al siguiente registro.')
                    # break
                except completeTypeError as error:
                    print(f'Error: {error}\nDato ingresado no es correcto, no se puede agregar. Se continua al siguiente registro.')
                    # break
                except formatTypeError as error:
                    print(f'Error: {error}\nDato ingresado no es correcto, no se puede agregar. Se continua al siguiente registro.')
                    # break
                except  ValueError as error:
                    print(f'Error: {error}\nDato ingresado no es correcto, no se puede agregar. Se continua al siguiente registro.')
                    # break    
            print(f'Se completa proceso de importar CSV Se actualiza la lista de estudiantes.')
            show_all_students(new_std_list)            
            return new_std_list
    except Exception as e:
        print(f'Error en funcion para importar datos a CSV. Error: {e}')

# Funcion para exportar los datos a CSV y validar la lista actual en CSV uniendo los datos
def ftn_csv_export_memoria(student_list,path_csv_file):
    try:
        # path_file_csv = 'Control_Estudiantes/Estudiantes.csv' 
        headers=[]
        i=0
        std_data = read_csv_file(path_csv_file) 
        # std_data = student_list
        if not std_data:
            headers = HEATHERS_FILE
        else:
            for item  in std_data[0].keys():
                headers.append(item)
            for item in std_data:
                i+=1
                print(f'El estudiante en CSV es {i} - {item['name']}')
                while True:
                    try:
                        student_name = no_duplicate_student(validate_complete_name(validate_empty_name(validate_name(item['name']))),student_list)
                        student_section = validate_section_format(item['section'])
                        spanish_grade = grade_number(item['spanish_grade'])
                        english_grade = grade_number(item['english_grade'])
                        social_grade = grade_number(item['social_grade'])
                        science_grade = grade_number(item['science_grade'])
                        new_student = {
                            "name": student_name,
                            "section":student_section,
                            "spanish_grade": spanish_grade,
                            "english_grade":english_grade,
                            "social_grade":social_grade,
                            "science_grade":science_grade
                            }
                        student_list.append(new_student)
                    except nameTypeError as error:
                        print(f'Error: {error}\nDato ingresado no es correcto, no se puede agregar. Se continua al siguiente registro.')
                        break
                    except emptyTypeError as error:
                        print(f'Error: {error}\nDato ingresado no es correcto, no se puede agregar. Se continua al siguiente registro.')
                        break
                    except completeTypeError as error:
                        print(f'Error: {error}\nDato ingresado no es correcto, no se puede agregar. Se continua al siguiente registro.')
                        break
                    except formatTypeError as error:
                        print(f'Error: {error}\nDato ingresado no es correcto, no se puede agregar. Se continua al siguiente registro.')
                        break
                    except  ValueError as error:
                        print(f'Error: {error}\nDato ingresado no es correcto, no se puede agregar. Se continua al siguiente registro.')
                        break            
        data.csv_export(path_csv_file,student_list, headers)
    except Exception as e:
        print(f'Error en funcion para exportar datos a CSV. Error: {e}')

    