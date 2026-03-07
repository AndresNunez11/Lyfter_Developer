
import csv
path = 'csvejercio#1.csv'
path1 = 'csvejercio#2.csv'
my_data = []

"""
Cree un programa que abra un archivo .csv con la información de videojuegos (el que fue generado en el ejercicio 1) y:
Lea cada línea usando csv.reader()
Muestre el contenido en pantalla de forma legible, línea por línea
Ejemplo:
Salida:
Nombre: Grand Theft Auto IV
Género: Accion
Desarrollador: Rockstar Games
Clasificación: M
"""
def read_csvfile(filepath):
    try:
        i=0
        with open(filepath,'r', newline="", encoding='utf-8')as file:
            reader= csv.DictReader(file)
            for row in reader:
                i+=1
                print(f'Linea #{i}')
                print(f"Nombre: {row['nombre']}")
                print(f"Género: {row['genero']}")
                print(f"Desarrollador: {row['desarrollador']}")
                print(f"Clasificación: {row['clasificacion']}")
                # my_data.append(row)
            # return my_data
            # print(my_data)
    except Exception as e:
        print(f'Error al leer archivo {e}')



"""
Cree un programa que abra un archivo .csv con la información de videojuegos ( en base al CSV que fue generado en el ejercicio 1) y:
Lea el archivo CSV de videojuegos
Pida al usuario una clasificación ESRB (por ejemplo: "T")
Muestre todos los videojuegos que tengan esa clasificación
"""

def filter_read_csvfile(filepath):
    try:
        clasificacion_buscada = input("Ingrese la clasificación ESRB (Ej: E, T, M): ").upper()
        print("\nVideojuegos con clasificación", clasificacion_buscada)
        i=0
        Encontrado = False
        with open(filepath,'r', newline="", encoding='utf-8')as file:
            reader= csv.DictReader(file)
            for row in reader:
                if(row['clasificacion'].upper() == clasificacion_buscada):
                    i+=1
                    print(f'Linea #{i}')
                    print(f"Nombre: {row['nombre']}")
                    print(f"Género: {row['genero']}")
                    print(f"Desarrollador: {row['desarrollador']}")
                    print(f"Clasificación: {row['clasificacion']}")
                    Encontrado = True
            if not Encontrado:
                print(f'No hay vodeojuegos con clasificacion {clasificacion_buscada}')
                # my_data.append(row)
            # return my_data
            # print(my_data)
    except Exception as e:
        print(f'Error al leer y filtrar archivo {e}')

"""
Cree un programa que abra un archivo .csv con la información de videojuegos ( en base al CSV que fue generado en el ejercicio 1) y:
Lea el archivo .csv con videojuegos
Cuente cuántos videojuegos hay de cada género
Muestre el resultado de forma ordenada
Ejemplo:
Salida:
Géneros encontrados:
Acción: 5
Aventura: 3
Deportes: 4
"""

def genre_game_csvfile(filepath):
    try:
        count_genre = {}       
        with open(filepath,'r', newline="", encoding='utf-8')as file:
            reader = csv.DictReader(file)
            for row in reader:
                genre = row["genero"]
                if genre in count_genre:
                    count_genre[genre] +=1
                else:
                    count_genre[genre] =1
        for genre in sorted(count_genre):
            print(f"{genre}: {count_genre[genre]}")
    except Exception as e:
        print(f'Error al agrupar por genero archivo {e}')


"""
Cree un programa que abra un archivo .csv con la información de videojuegos( en base al CSV que fue generado en el ejercicio 1) y:
Lea el archivo .csv con videojuegos
Pida al usuario ingresar el nombre de un desarrollador (ej. "Ubisoft")
Muestre todos los videojuegos desarrollados por esa empresa en formato legible:
Ejemplo:
Salida:
Videojuegos desarrollados por Ubisoft:
- Assassin's Creed II (Clasificación: M, Género: Aventura)
- Rayman Legends (Clasificación: E, Género: Plataforma)
"""

def filter_dev_read_csvfile(filepath):
    try:
        dev = input("Ingrese la nombre del desarrollador \n").upper()
        print("Videojuegos con Desarrollador", dev)
        i=0
        found = False
        with open(filepath,'r', newline="", encoding='utf-8')as file:
            reader= csv.DictReader(file)
            for row in reader:
                if(row['desarrollador'].upper() == dev):
                    i+=1
                    print(f'Linea #{i}')
                    print(f"Nombre: {row['nombre']}")
                    print(f"Género: {row['genero']}")
                    print(f"Desarrollador: {row['desarrollador']}")
                    print(f"Clasificación: {row['clasificacion']}")
                    found = True
            if not found:
                print(f'No hay vodeojuegos desarrollador por {dev}')
                # my_data.append(row)
            # return my_data
            # print(my_data)
    except Exception as e:
        print(f'Error al leer y filtrar desarrollador {e}')






def main():
    try:
        # print('Ejercicio #1')
        # read_csvfile(path)
        # print('Ejercicio #2')
        # filter_read_csvfile(path)
        # print('Ejercicio #3')
        # genre_game_csvfile(path)
        print('Ejercicio #4')
        filter_dev_read_csvfile(path)
        
    except Exception as e:
        print(f'Error al ejecutar el proceso principal, {e}')

main()