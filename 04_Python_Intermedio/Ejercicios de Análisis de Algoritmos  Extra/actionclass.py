from inidataclass import Datos
from analistexerciseone import ExerciseOne
from analistexercisetwo import ExerciseTwo
from analistexercisethree import ExerciseThree


# import inidataclass
class Menu_Actions(Datos):

#Constructor
    def __init__(self, path):
        # self.contador = 0
        self.path = path
        self.balance = 0
        
#Mostrar el Menu principal
    def show_menu(self):
        for index, exercise in enumerate(self.list_exercise) :
            print(f'{index} - {exercise} \n')    
            # self.contador+=1  

#Respuesta ejercicio #1
    def answer_exercise1(self):
        ExerciseOne.print_answer(self)

#Respuesta ejercicio #2
    def answer_exercise2(self):
        ExerciseTwo.print_answer(self)

#Respuesta ejercicio #3
    def answer_exercise3(self):
        ExerciseThree.print_answer(self)




