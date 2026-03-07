"""
Cree un programa que lea nombres de canciones de un archivo (línea por línea) 
y guarde en otro archivo los mismos nombres ordenados alfabéticamente.
"""


def open_file(path):   
    try:
        with open(path, encoding='utf-8') as file:
            my_file= file.read()
            return my_file            
    except Exception as e:
        print(f'Error al abrir al archivo {e}')
    
def read_order_file(document):
    try:
        my_list = []
        for line in document.split("\n"):
            my_list.append(line)
        my_list.sort()
        # for line in document.split("\n"):
        #     if(counter == 0):
        #         my_list.append(line)
        #     elif(line < my_list[0]):
        #         my_list.insert(0, line)
        #     else:
        #         index = 0
        #         large = len(my_list)-1
        #         try:
        #             while index <= large:
        #                 if(line > my_list[large]):
        #                     my_list.append(line)
        #                     break
        #                 elif(line > my_list[index] and line < my_list[index+1]):
        #                     my_list.insert(index+1, line)
        #         except IndexError as e:
        #                 print(f'El indice a usar no existe en la lista. Error: {error}')
        #         index+=1
        #     counter+=1
        return (my_list)
    except Exception as e:
        print(f'Error al leer el archivo {e}')

def write_file(path2, list):
    try:
        with open(path2, 'w', encoding='utf-8') as file:
            for item  in list:
                file.write(f'{item} \n')
        
        
        # with open(path2) as file:
        #     read_file = file.read()
        # if(read_file == ''):
        #     for item  in list:
        #         with open(path2, 'a') as file:
        #             file.write(f'{item} \n')
        # else:           
        #     with open(path2, 'w') as file:
        #         pass
        #     for item  in list:
        #         with open(path2, 'a') as file:
        #             file.write(f'{item} \n')
        print('Archivo modificado correctamente')
    except Exception as e:
        print(f'Error en el proceso de escritura: {e}')

"""
Lea sobre el resto de métodos de la clase File de Python aquí y cree una tabla donde explique qué hace cada uno. 
No necesita usar código para esto, es solo crear una tabla en Notion o Word.
Siga el siguiente formato:
Método	Descripción
read()	Lee y retorna todo el contenido del archivo
readlines()	Lee todo el contenido del archivo y retorna una lista con cada línea.
write()	Escribe contenidos en un archivo.

Docstring for Ejercicios_Manejo_Archivos
"""





# Principal process of an exercises

def main():
    try:
        path = 'NombreCanciones.txt'
        path2 = 'NombreCancionesOrdenadas.txt'
        print('Ejercicio 1')
        example_file = open_file(path)
        file_list = read_order_file(example_file)
        write_file(path2, file_list)
    except Exception as e:
        print(f'Error en el proceso principal: {e}')

    
main()