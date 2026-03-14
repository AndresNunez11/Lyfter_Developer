import data
#variables globales
student_list= []

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
    for student in std_list:
        if enter_text == student['name']:
            raise ValueError("El estudiante ya fue agregado a la lista de estudiantes")
    return enter_text

# Funcion para leer los datos desde Jason, utilizando modulo de data
def read_json_file(path_json_file):
    student_list = data.read_json_file(path_json_file)
    return student_list

# Funcion para agregar a un nuevo estudiante a la base de estudiantes
def new_student(path_json_file):
    while True:
        try: 
            new_student_list = read_json_file(path_json_file) or []       
            #new_student_list = student_list or []
            student_name = no_duplicate_student(input('Ingrese el nombre completo del estudiante: \n'),new_student_list)
            student_section= input('Ingresa el numero de seccion del estudiante: \n')
            spanish_grade = grade_number(int(input('Ingresa la nota para la asignacion - Español: \n')))
            english_grade = grade_number(int(input('Ingresa la nota para la asignacion - Ingles: \n')))
            social_grade = grade_number(int(input('Ingresa la nota para la asignacion - Estudios Sociales: \n')))
            science_grade = grade_number(int(input('Ingresa la nota para la asignacion - Ciencias: \n')))
            new_student = {
                "name": student_name,
                "section":student_section,
                "spanish_grade": spanish_grade,
                "english_grade":english_grade,
                "social_grade":social_grade,
                "science_grade":science_grade
                }
            new_student_list.append(new_student)
            data.save_new_student(new_student_list,path_json_file)
            desicion = input(f'Estudiante agregadoa la base de estudianetes. para agregar otro estudiante digite Y o para salir digite N -> ').upper()
            if desicion == 'N':
                break
        except  ValueError as error:
            print(f'Error: {error}\nDato ingresado no es correcto. Intente nuevamente.')
            desicion = input(f'Para continuar con el ingreso de estudiantes digite Y o para salir digite N -> ').upper()
            if desicion == 'N':
                break
        except Exception as e:
            print(f'Existe un error al ingresar el nuevo estudiante. Error: {e}')

# Funcion para mostrar la informacion de los estudiantes registrados en la base de estudiantes
def show_all_students(path_json_file):
    try:
        new_std_list = read_json_file(path_json_file)
        i=0
        for student in new_std_list:
            i+=1
            print(f'Estudiante # {i}')
            print(student)
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
def top_3_average(path_json_file):
    try:
        sort_list = []
        new_std_list = read_json_file(path_json_file)
        for student in new_std_list:
            grade_average = (student['spanish_grade']+student['english_grade']+student['social_grade']+student['science_grade'])/4
            new_student = {
                'name': student['name'],
                'section': student['section'],
                'average':grade_average}
            sort_list.append(new_student)
        sort_list.sort(key=lambda s: s["average"], reverse=True) # funcion que le indica al diccionario como debe de ordenarse, en este caso por el promedio
        top_3 = sort_list[:3]
        print(top_3)
    except Exception as e:
        print(f'Error al obtener el top 3 en promedio de notas. Error: {e} ')

# Funcion para calcular el promedio total de todos los estudantes (std = student  // stds students)
def total_average(path_json_file):
    try:
        std_list = read_json_file(path_json_file)
        new_std_list = []
        for student in std_list:
            grade_average = (student['spanish_grade']+student['english_grade']+student['social_grade']+student['science_grade'])/4
            new_student = {
                'name': student['name'],
                'section': student['section'],
                'average':grade_average}
            new_std_list.append(new_student)
        index = len(new_std_list)
        stds_average = 0
        for std in new_std_list:
            stds_average=stds_average + std['average']
        total_average = stds_average / index
        print(f"Total de estudiantes: {index}\n Promedio ponderado de notas : {total_average}" )
    except Exception as e:
        print(f'Error al obtener el  promedio total de notas de todos los estudiantes. Error: {e} ')

# Funcion para exportar los datos a CSV
def ftn_csv_export(path_json_file):
    try:
        path_file_csv = 'Control_Estudiantes/Estudiantes.csv' 
        headers=[]
        std_data = read_json_file(path_json_file)
        for item  in std_data[0].keys():
            headers.append(item)
        data.csv_export(path_file_csv,std_data, headers)
    except Exception as e:
        print(f'Error en funcion para exportar datos a CSV. Error: {e}')

# Funcion para importar los datos a CSV
def ftn_csv_import():
    try:
        path_file_csv = 'Control_Estudiantes/Estudiantes.csv' 
        data.csv_import(path_file_csv)        
    except Exception as e:
        print(f'Error en funcion para exportar datos a CSV. Error: {e}')