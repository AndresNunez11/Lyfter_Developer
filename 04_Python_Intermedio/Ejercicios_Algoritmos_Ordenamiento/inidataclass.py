
import json
from exerciseclass import Exercise
from listexerciseslass import List_Exercises 

#Clase Hija que herada de ejercicio y list de ejercicios

class Datos(Exercise, List_Exercises):
    
    
    #Variables Globales inmutables
    HEATHERS_FILE = ["description"]

    def __init__(self, path):
        self.path = path
        

    # Leer archivo de Json con informacion de ejercicio, si no existe crea el archivo
    def read_json_file(self):
        self.list_exercise= []
        try:
            with open(self.path, "r", encoding="utf-8" ) as file:
                data = json.load(file)
                if (data, list):
                    for item in data:
                        # print(item)
                        self.description = item['description']
                        # print(self.description)
                        self.add_exercise(self.description)
                        # return self.list_exercise
                        # print(self.list_exercise)
                else:                    
                    return self.list_exercise  
        except FileNotFoundError:
            print(f"Archivo no encontrado, se creará uno nuevo {self.path}")
            return self.list_exercise
        except json.JSONDecodeError:
            print("Archivo JSON corrupto, se inicia con lista vacía")
            return self.list_exercise
        except Exception as e:
            print(f'Error al leer archivo JSON {e}')
            


