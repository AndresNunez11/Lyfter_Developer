from inidataclass import Datos
from bubblesortclass import BublleSort

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

#1 - Algoritmo de ordenamiento
    def bubble_sort_list(self):
        my_list = [9,5,4,3,8,7,6,1,2]
        print(f'Lista Inicial')
        print(f'{my_list}')
        new_list_sort = BublleSort(my_list)
        my_list = new_list_sort.bubble_sort_list()
        print('Lista Ordenada')
        print(f'{my_list}')
        my_second_list = [9,1,2,3,4,5,8,7,6,]
        print(f'Lista Inicial')
        print(f'{my_second_list}')
        new_list_sort = BublleSort(my_second_list)
        my_second_list = new_list_sort.bubble_sort_list()
        print('Lista Ordenada')
        print(f'{my_second_list}')

#2 - Algoritmo de ordenamiento reverso

    def reverse_bubble_sort_list(self):
            my_list = [9,5,4,3,8,7,6,1,2]
            print(f'Lista Inicial')
            print(f'{my_list}')
            new_list_sort = BublleSort(my_list)
            my_list = new_list_sort.reverse_bubble_sort_list()
            print('Lista Ordenada')
            print(f'{my_list}')
            my_second_list = [9,1,2,3,4,5,8,7,6,]
            print(f'Lista Inicial')
            print(f'{my_second_list}')
            new_list_sort = BublleSort(my_second_list)
            my_second_list = new_list_sort.reverse_bubble_sort_list()
            print('Lista Ordenada')
            print(f'{my_second_list}')
    