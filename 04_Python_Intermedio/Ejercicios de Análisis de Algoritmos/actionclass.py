from inidataclass import Datos
from validatebubblesort import validateBubblesort
from validateotherexercises import ValidateExercises

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
            print(f'{index} - {exercise}')    
            # self.contador+=1  

    def bubblesort_analist(self):
        validateBubblesort.bubblesortanalist(self)

    def other_exercises_analist(self):
        ValidateExercises.exercises_analist(self)


