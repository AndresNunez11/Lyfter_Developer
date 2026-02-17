import json

# Variables Globales
path_file = 'archivojson.json' 

# Validaciones
def no_spaces_text(enter_text):
    if " " in enter_text:
        raise ValueError("El texto no debe contener espacios en blanco")
    return enter_text

# Leer archivo JSON
def read_jason_file(path):
    pokemon_list = []
    try:
        with open(path, "r", encoding="utf-8" ) as file:
            data = json.load(file)
            if (data, list):
                pokemon_list = data
                print(f'Lista Inicial leida con exito')
                # print(f'Lista inicial de pokemones tomada de archivo json \n{pokemon_list}')
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

"""
Cree un programa que abra un archivo .json con la información de Pokémon 
( en base al JSON que fue generado en el ejercicio 1) y:
Lea el archivo JSON de Pokémon
Recorra la lista de Pokémon y muestre en consola su nombre, tipo y nivel 
(o cualquier otro atributo definido)
Cree un programa que abra un archivo .json con la información de Pokémon 
( en base al JSON que fue generado en el ejercicio 1) y:
Lea el archivo JSON de Pokémon
Pida al usuario un tipo de Pokémon
Muestre todos los Pokémon que sean de ese tipo
Ejemplo:
Entrada:
"Ingrese el tipo de pokemon desea buscar(agua,electrico,fuego,etc): "
"Fuego"
Salida:
"Los pokemos que existen de ese tipo son: "
Charmander
Growlithe
Victini
"""
def show_pokemon(pokemon_list):
    try:
        print(f'1.1 - Recorra la lista de Pokémon y muestre en consola su nombre, tipo y nivel \n')
        for pokemon in pokemon_list:
            name = pokemon["name"]["english"]
            type = pokemon["type"]
            level = pokemon["level"]
            # Si type es una lista, la convertimos a texto
            if isinstance(type, list):
                type = ", ".join(type)
            if isinstance(level, list):
                level = ", ".join(level)
            print(f'Nombre: {name}')
            print(f'Tipo: {type}')
            print(f'Nivel: {level}')
    except Exception as e:
        print(f'Error al mostrar los datos del pokemon {e}')


def filter_type(pokemon_list):
    while True: 
        try:
            types = []
            my_new_pokemon_list = []
            print(f'1.2 - Cree un programa que abra un archivo .json con la información de Pokémon. Lea el archivo JSON de Pokémon\n Pida al usuario un tipo de Pokémon Muestre todos los Pokémon que sean de ese tipo')
            for pokemon in pokemon_list:
                type = pokemon["type"]
                if isinstance(type, list):
                    for item in type:
                        types.append(item)
                else:
                    types.append(type)
            search_type= no_spaces_text(input(f'Ingrese el tipo de pokemon desea buscar({types}):'))
            for pokemon in pokemon_list:
                type = pokemon["type"]
                if isinstance(type, list):
                    for item in type:
                        if(item == search_type):
                            my_new_pokemon_list.append(pokemon)
                        elif type == search_type:
                            my_new_pokemon_list.append(pokemon)
            print(f'Los pokemos que existen de ese tipo {search_type} son:')
            # print(f'{my_new_pokemon_list}')
            for pokemon in my_new_pokemon_list:
                print(f'{pokemon["name"]["english"]}')
            decision = input(f'Para otra consulta digite Y. para continuar digite cualquier otra tecla.')
            if(decision.upper() != 'Y'):
                break
        except ValueError as error:
            print(f'Error: {error}\nDato ingresado no es correcto. Intente nuevamente.')
        except Exception as e:
            print(f'Error en el proceso de filtrar por tipo de pokemos. {e}')

"""
Cree un programa que abra un archivo .json con la información de Pokémon 
( en base al JSON que fue generado en el ejercicio 1) y:
Lea el archivo JSON de Pokémon
Para cada Pokémon, muestre sus estadísticas principales (por ejemplo: ataque, defensa, velocidad, etc.)
Ejemplo:
Salida:
Nombre: Pikachu
Ataque: 55
Defensa: 40
Velocidad: 90
Nombre: Bulbasaur
Ataque: 49
Defensa: 49
Velocidad: 45
"""

def feature_pokemons(pokemon_list):
    try:
        print(f'2 - Cree un programa que abra un archivo .json, Lea el archivo JSON de Pokémon Para cada Pokémon, muestre sus estadísticas principales (por ejemplo: ataque, defensa, velocidad, etc.)\n')
        for pokemon in pokemon_list:
            type = pokemon["type"]
            print(f'Nombre: {pokemon["name"]["english"]}')
            print(f'Ataque: {pokemon["base"]["Attack"]}')
            print(f'Defensa: {pokemon["base"]["Defense"]}')
            print(f'Velocidad: {pokemon["base"]["Speed"]} \n')
    except Exception as e:
            print(f'Error en al mostrar caracteristicas del pokemos. {e}')



"""
Cree un programa que abra un archivo .json con la información de Pokémon ( en base al JSON que fue generado en el ejercicio 1) y:
Lea el archivo JSON
Agrupe los Pokémon por tipo (por ejemplo, "agua", "fuego", etc.)
Calcule y muestre el promedio de nivel para cada tipo:
Ejemplo:
Salida:
Tipo: Agua → Promedio de nivel: 42.6
Tipo: Fuego → Promedio de nivel: 37.2
Tipo: Planta → Promedio de nivel: 30.4
"""
def average_type(pokemon_list):
    try:
        types = {}
        for pokemon in pokemon_list:
            pokemon_types = pokemon["type"] 
            level = pokemon["level"]  
            # print(pokemon_types)    
            for type in pokemon_types:
                if(type in types):
                    # print(f"{pokemon_types} ya agregado a types")
                    types[type]['total']=types[type]['total'] + level
                    types[type]['quantity']= types[type]['quantity'] + 1
                else: 
                    types[type] ={
                        "total": 0,
                        "quantity": 0
                    }
                    types[type]['total']=+level
                    types[type]['quantity']=+1
            # print(types)
        for type in types:
            print(f'Tipo: {type} → Promedio de nivel: {types[type]["total"]/types[type]["quantity"]} ')

            

    except Exception as e:
        print(f'Error al agrupar por tipo {e}')




def main():
    try:
        pokemon_list = read_jason_file(path_file)
        print(f'Ejercicio #1')
        show_pokemon(pokemon_list)
        filter_type(pokemon_list)
        print(f'Ejercicio #2')
        feature_pokemons(pokemon_list)
        print(f'Ejercicio #3')
        average_type(pokemon_list)
    except Exception as e:
        print(f'Error en el proceso principal {e}')

if __name__ == "__main__":
    main()
        


