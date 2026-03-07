"""
Cree un programa que lea un archivo con texto línea por línea, 
quite los saltos de línea (\n) y escriba todo el contenido en un solo renglón en 
un nuevo archivo
Ejemplo:
Entrada:
Copiar
Hola
mundo
esto
es
Python
Salida:
"Hola mundo esto es Python"
"""

def open_file(path):
    try:
        with open(path, encoding='utf-8') as file:
            'print(file.read())'
            return file.read()
    except Exception as e:
        print(f'Error al abrir al archivo {e}')

def read_file(document):
    try:
        my_string = ''
        for line in document.split("\n"):
            if(my_string == ''):
                my_string = line
            else:
                my_string = my_string +" "+ line
        # print(my_string)
        return my_string
    except Exception as e:
        print(f'Error al leer cada linea del archivo')

def write_file(path4,string):
    try:
        with open(path4, 'w', encoding="utf-8") as file:
            pass
            file.write(string)
        print('Archivo modificado correctamente')
    except Exception as e:
        print(f'Error en el proceso de escritura: {e}')


"""
Cree un programa que abra un archivo de texto y cuente cuántas palabras contiene en total.
(Considere que las palabras están separadas por espacios y/o saltos de línea)
Ejemplo:
Salida:
"Este archivo contiene "
123
"palabras"
"""

def count_words(document):
    try:
        words =  document.split()
        counter = len(words)
        print(f'La cantidad de palabras en el archiv es de: {counter} palabras')
    except Exception  as e:
        print(f'Existe un error al contar las palabras {e}')

"""
Cree un programa que:
Lea un archivo línea por línea
Convierta cada línea a mayúsculas
Escriba el contenido en un nuevo archivo
Ejemplo:
Entrada:
# archivo original:
hola mundo
esto es python
Salida:
# archivo nuevo:
HOLA MUNDO
ESTO ES PYTHON
"""
def uppercase(file):
    try:
        with open(file, 'r', encoding="utf-8") as document:
            lines = document.readlines()
        with open('EjercicioMayuscutas.txt', 'w', encoding="utf-8") as new_document:
            for line in lines:
                new_document.write(line.upper())
        print('Archivo creado correctamente')
    except Exception  as e:
        print(f'Existe un error al pasar a mayusculas el archivo {e}')
"""
Cree un programa que:
Pida al usuario una línea de texto
Agregue esa línea al final de un archivo existente
Si el archivo no existe, lo crea automáticamente
Ejemplo:
Entrada:
"Este es un nuevo registro"
Salida:
"El texto se agrega al final del archivo sin borrar lo anterior"
"""

# class nameTypeError(Exception):
#     def __init__(self,name):
#         super().__init__(f'\n El nombre no puede ser o incluir un número')

def input_text():
    try:
        text = input('Ingrese un texto\n')
        return text
    except Exception as e:
        print(f"Error detectado: {e}")

def write_newfile(path3, text):
            try:
                with open(path3, "a", encoding="utf-8") as document:
                    document.write(text + '\n')
                    print(f'Palabra {text} agregada correctamente')        
            except Exception as e:
                    print(f'Error en el proceso de escritura: {e}')
def cycle(path3):
    while True:
        try:
            text = input_text()
            if text == "":
                print("No se ingreso un texto.Proceso finalizado.")
                break
            else:
                write_newfile(path3, text)
        except Exception as e:
            print(f'Error en el ciclo de escritura {e}')




def main():
    try:
        path = 'Manejo_Archivos_extra.txt'
        path1='archivoejercicio1.txt'
        path2 = 'CantidadPalabras.txt'
        path3 = 'NuevoArchivo.txt'        
        print('Ejercicio #1')
        write_file(path1,read_file(open_file(path)))
        print('Ejercicio #2')
        file2 = open_file(path2)
        count_words(file2)
        print('Ejercicio #3')
        uppercase(path)
        print('Ejercicio #4')
        cycle(path3)
    except Exception as e:
        print(f'Error en el proceso central {e}')

main()