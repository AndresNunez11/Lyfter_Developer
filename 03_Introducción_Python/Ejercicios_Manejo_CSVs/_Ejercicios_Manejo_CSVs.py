import csv

"""
Cree un programa que me permita ingresar información de n cantidad de videojuegos 
y los guarde en un archivo csv.
Debe incluir:
Nombre
Género
Desarrollador
Clasificación ESRB

Ejemplo de archivo final:
nombre,genero,desarrollador,clasificacion
Grand Theft Auto IV,Accion,Rockstar Games,M
The Elder Scrolls IV: Oblivion,RPG,Bethesda,M
Tony Hawk's Pro Skater 2,Deportes,Activision,T
"""
mydata = [
    {
    'nombre': 'Grand Theft Auto IV',
    'genero': 'Accion',
    'desarrollador': 'Rockstar',
    'clasificacion': 'M',
    },
    {
    'nombre': "Tony Hawk's Pro Skater 2",
    'genero': 'Deportes',
    'desarrollador': 'Actiision',
    'clasificacion': 'T',
    },
    {
    'nombre': 'The Elder Scrolls IV: Oblivion',
    'genero': 'RPG',
    'desarrollador': 'Bethesda',
    'clasificacion': 'M',
    },
]


# Para mantener el orden a la hora de generar el csv, se debe mantener los headers en un lista que mantine el orden
# no cmo los diccionarios o sets que pueden variar el orden.  {} - > []
myheaders = [
    'nombre',
    'genero',
    'desarrollador',
    'clasificacion'
]

def add_data():
    try:
        mydictionary = {}
        name = input('Ingrese en nombre de VideoJuego \n')
        game_genre = input('Ingrese en genero de VideoJuego \n')
        dev= input('Ingrese en desarrollador de VideoJuego \n')
        classification = input('Ingrese en clasificacion de VideoJuego \n')
        mydictionary['nombre'] = name
        mydictionary['genero'] = game_genre
        mydictionary['desarrollador'] = dev
        mydictionary['clasificacion'] = classification        
        mydata.append(mydictionary)
        # print(mydata)
        return mydictionary
    except Exception as e:
        print(f'Error en el proceso de agregar datos {e}')

def writecsv(filepath, data, myheaders):
    try:
        with open(filepath, 'w', newline="", encoding='utf-8')as file:
            writer= csv.DictWriter(file, myheaders)
            writer.writeheader()
            writer.writerows(data)
    except Exception as e:
        print(f'Error al guardar archivo csv 1 {e}')
"""
Lea sobre el resto de métodos del módulo csv aqui y 
cree una version alternativa del ejercicio de arriba que guarde
el archivo separado por tabulaciones en vez de por comas.
Ejemplo de archivo final:

nombre	genero	desarrollador	clasificacion
Grand Theft Auto IV	Accion	Rockstar Games	M
The Elder Scrolls IV: Oblivion	RPG	Bethesda	M

"""
def writercsv2(filepath, data, headers):
    try:
        with open(filepath, 'w', newline="", encoding='utf-8')as file:
            writer= csv.DictWriter(file, headers, delimiter='\t')
            writer.writeheader()
            writer.writerows(data)  
    except Exception as e:
        print(f'Error al guardar archivo csv2 {e}')

"""
El módulo csv permite leer y escribir archivos de texto estructurados en forma de tablas, 
donde los datos están separados por un delimitador:
Coma , → CSV clásico
Tabulación \t → TSV
Punto y coma ; → Muy común en Excel (configuración regional)
El módulo se encarga de:
Separar columnas correctamente
Manejar comillas
Evitar errores con saltos de línea
Escribir archivos compatibles con Excel y otros sistemas



| Método         | Uso                    |
| -------------- | ---------------------- |
| `writer()`     | Escribir listas        | -- Crea un objeto escritor que permite escribir filas usando listas o tuplas.
| `DictWriter()` | Escribir diccionarios  | -- Permite escribir filas usando diccionarios en lugar de listas.
| `writerow()`   | Una fila               | -- Escribe una sola fila en el archivo.
| `writerows()`  | Varias filas           | -- Escribe varias filas a la vez.
| `delimiter`    | Separador              | -- Define el separador entre columnas. , \t ;
| `reader()`     | Leer como listas       | -- Lee el archivo línea por línea y devuelve listas.
| `DictReader()` | Leer como diccionarios | -- Lee el archivo y devuelve diccionarios.

newline=""  -- Evita que Windows agregue líneas en blanco entre filas.
DictWriter.writeheader() -- Escribe automáticamente la fila de encabezados.
DictWriter.writerow() -- Escribe una fila desde un diccionario.
DictWriter.writerows() -- Escribe varios diccionarios a la vez.

quotechar -- Define el carácter para encerrar texto
    csv.writer(archivo, quotechar='"')
quoting --  Controla cuándo usar comillas 
    csv.QUOTE_ALL        # Comillas en todo
    csv.QUOTE_MINIMAL    # Solo cuando es necesario (default)
escapechar -- Para escapar caracteres especiales
    csv.writer(archivo, escapechar="\\")

"""






def main():
    try:        
        path = 'csvejercio#1.csv'
        path1 = 'csvejercio#2.csv'
        instruction = 'y'
        while instruction == 'y':
            add_data()
            instruction = input(f'Digite "y" para ingresar otro dato. "n" para terminar \n')
        writecsv(path, mydata, myheaders)
        writercsv2(path1, mydata, myheaders)
        print('Ejericio # 1')
        print(f'Datos ingresado se agrega a csv \n {path}')
        print('Ejericio # 2')        
        print(f'Datos ingresado se agrega a csv2 \n {path1}')
    except Exception  as e:
        print(f'Existe un error en la ejecucion principal {e} ')


main()