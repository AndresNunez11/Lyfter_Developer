import json

# Variables Globales
path_file = 'archivojson_nuevo1.json' 


# Excepciones

# Excepcion en numeros menores a cero
def no_negative_number(enter_number):
    if enter_number < 0:
        raise ValueError("El número no puede ser menor que cero")
    return enter_number

# Notas importantes para validar espacios
"""
**------------------------------------------------------**
Usa isspace() para detectar cualquier carácter en blanco:
if any(c.isspace() for c in texto):
        raise ValueError("El texto no debe contener espacios en blanco")
    return texto
Si solo quieres evitar espacios antes o después:
if texto != texto.strip():
    raise ValueError("No se permiten espacios al inicio o al final")
**------------------------------------------------------**
"""
# Excepcion para no ingresar espacion en el nombre o tipo
def no_spaces_text(enter_text):
    if " " in enter_text:
        raise ValueError("El texto no debe contener espacios en blanco")
    return enter_text


"""
1- Investigue cómo leer y escribir archivos JSON en Python aquí.
"""
# If you have a JSON string, you can parse it by using the json.loads() method.
# If you have a Python object, you can convert it into a JSON string by using 
# the json.dumps() method.
# Use the indent parameter to define the numbers of indents:

'''

Acción	                | Método
Leer archivo JSON	    | json.load()
Escribir archivo JSON	| json.dump()
JSON a string	        | json.dumps()
String a JSON	        | json.loads()

'''


"""
2- Cree un programa que permita agregar un Pokémon nuevo al archivo de la lección de JSON (https://learning.lyfter.team/dashboard/roadmap/fffab4f1-5c3f-480a-9671-ae1a235c3b6a/dac6b243-2cab-496f-96de-5debb9ce613e)
    1- Debe leer el archivo para importar los Pokémones existentes.
    2- Luego debe pedir la información del Pokémon a agregar.
    3- Finalmente debe guardar el nuevo Pokémon en el archivo.
"""
def read_json_file(path):
    pokemon_list = []
    try:
        with open(path, "r", encoding="utf-8" ) as file:
            data = json.load(file)
            if (data, list):
                pokemon_list = data
                print(f'Lista inicial de pokemones tomada de archivo json \n{pokemon_list}')
                return pokemon_list
            else:
                return pokemon_list  
    except FileNotFoundError:
        print("Archivo no encontrado, se creará uno nuevo")
        return pokemon_list
    except json.JSONDecodeError:
        print("Archivo JSON corrupto, se inicia con lista vacía")
        return pokemon_list
    except Exception as e:
        print(f'Error al leer archivo JSON {e}')
        

def new_pokemon(pokemon_list):
    while True:
        new_pokemon_list = []
        try:        
            type_list = []
            new_pokemon_list = pokemon_list
            name = no_spaces_text(input('Ingrese el nombnre del pokemon \n'))
            level = no_negative_number(int(input('Ingrese el nivel del pokemon \n')))
            decision = "Y"
            while decision.upper() == "Y":
                type = no_spaces_text(input('Ingrese el tipo de pokemon \n'))
                type_list.append(type)
                decision = input('Digete Y para agregar un nuevo tipo o N para finalizar \n')            
            HP = no_negative_number(int(input('Ingrese el HP de pokemon \n')))
            attack = no_negative_number(int(input('Ingrese el attack de pokemon \n')))
            defense = no_negative_number(int(input('Ingrese el defence de pokemon \n')))
            sp_attack =no_negative_number(int(input('Ingrese el Sp. Attack de pokemon \n')))
            sp_defense =no_negative_number(int(input('Ingrese el SP. defence de pokemon \n')))
            speed =no_negative_number(int(input('Ingrese el Speed de pokemon \n')))

            name_dic = {'english':name}
            base = {
                    'HP': HP,
                    "Attack": attack,
                    "Defense": defense,
                    "Sp. Attack":sp_attack,
                    "Sp. Defense":sp_defense,
                    "Speed": speed}
            new_pokemon_data = {
                    'name': name_dic,
                    'level': level,
                    'type':type_list,
                    'base': base
                }
            new_pokemon_list.append(new_pokemon_data)
            print(f'Pokemon agregado a la lista')
            # print(pokemon_list)
            # print(new_pokemon_list)
            return new_pokemon_list    
        except  ValueError as error:
                print(f'Error: {error}\nDato ingresado no es correcto. Intente nuevamente.')
                #Recursividad para que en caso de ingresar un dato erroneo, se reinicie el ingreso de datos
                # new_pokemon(pokemon_list) -- Sustituidad por un while
        except Exception as e:
            print(f'Error al ingresar datos de nuevo pokemon {e}')

def save_new_pokemon(pokemon_list, path):
    try:
        with open(path, "w", encoding="utf-8" ) as file:
            json.dump(pokemon_list, file, indent=4, ensure_ascii=False)
            # print(pokemon_list)
            print(f'Pokemon agregado al archivo')
    except Exception as e:
        print(f'Error al guardar nuevo pokemon {e}')


def main():
    try:
        print('*--------------------------------------* \n#1 - Debe leer el archivo para importar los Pokémones existentes.')
        pokemon_list = read_json_file(path_file)
        print('*--------------------------------------* \n#2 - Luego debe pedir la información del Pokémon a agregar.')
        print('#3 - Finalmente debe guardar el nuevo Pokémon en el archivo.')
        save_new_pokemon(new_pokemon(pokemon_list), path_file)
    except Exception as e:
        print(f'Error en el proceso principal {e}')


# “Ejecuta esto solo si este archivo es el que arranca el programa, no si es una librería”
"""
Evita ejecuciones no deseadas
Permite reutilizar funciones
Facilita pruebas unitarias
Es estándar profesional en Python
"""

if __name__ == "__main__":
    main()

