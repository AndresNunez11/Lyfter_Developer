from inidataclass import Datos
from nodoclass import Node
from linkedlistclass import LinkedList
from queueclass import Queue
from stackclass import Stack
from doubleendedqueueclass import DoubleEndedQueue
from binarytreeclas import BinaryTree


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

# Creando una Linked List
    def show_linked_list(self):
        firts_node = Node('Soy el primer nodo')
        second_node = Node('Soy el segundo nodo')
        third_node = Node('Soy el tercer nodo')
        firts_node.next = second_node
        second_node.next = third_node
        linked_list = LinkedList(firts_node)
        linked_list.print_structre()

# Creando una cola queue
    def show_queue(self):
        firts_node = Node('Soy el primer nodo')
        second_node = Node('Soy el segundo nodo')
        third_node = Node('Soy el tercer nodo')
        firts_node.next = second_node
        second_node.next = third_node
        newQueque =  Queue(firts_node)
        newQueque.print_structre()
        print('--Dequeue--')
        newQueque.dequeue()
        newQueque.print_structre()
        print('--Enqueue--')
        fourth_node = Node('Soy el cuarto nodo')
        newQueque.enqueue(fourth_node)
        newQueque.print_structre()
    
# Creando una cola stack
    def show_stack(self):
        firts_node = Node('Soy el primer nodo')
        second_node = Node('Soy el segundo nodo')
        third_node = Node('Soy el tercer nodo')
        firts_node.next = second_node
        second_node.next = third_node
        newStack=  Stack(firts_node)
        newStack.print_structre()
        print('\n--Push--')
        fourth_node = Node('Soy el cuarto nodo')
        newStack.push_stack(fourth_node)
        newStack.print_structre()
        print('\n--Pop--')
        newStack.pop_stack()
        newStack.print_structre()

# Creando una cola Double ended Queue
    def show_DobleEndedQueue(self):
        firts_node = Node('Soy el primer nodo')
        newDouEnQue = DoubleEndedQueue(firts_node)
        newDouEnQue.print_structre()
        print(f'\nSe relaciona primer Nodo y segundo Nodo')
        second_node = Node('Soy el segundo nodo')
        firts_node.next = second_node
        newDouEnQue.print_structre()
        print(f'\n---- Push Righ ---')
        first_righ_node = Node('Primer Nodo a la derecha')
        newDouEnQue.push_right(first_righ_node)
        newDouEnQue.print_structre()
        print(f'\nAgregando otro nodo')
        second_righ_node = Node('Segundo Nodo a la derecha')
        newDouEnQue.push_right(second_righ_node)
        newDouEnQue.print_structre()
        print(f'\n---- Push Left ---')
        first_left_node = Node('Primer Nodo a la izquierda')
        newDouEnQue.push_left(first_left_node)
        newDouEnQue.print_structre()
        print(f'\nAgregando otro nodo')
        second_left_node = Node('Segundo Nodo a la izquierda')
        newDouEnQue.push_left(second_left_node)
        newDouEnQue.print_structre()
        print(f'\n---- Pop right ---')
        newDouEnQue.pop_righ()
        newDouEnQue.print_structre()
        print(f'\n---- Pop left ---')
        newDouEnQue.pop_left()
        newDouEnQue.print_structre()
        print(f'-------Repite el Ciclo-------------')
        third_node_rigth = Node('tercer Nodo a la derecha')
        third_node_left = Node('tercer nodo a la izquierda')
        print('\nAgrega los nodos')
        newDouEnQue.push_right(third_node_rigth) 
        newDouEnQue.print_structre() 
        print('\n')
        newDouEnQue.push_left(third_node_left)
        newDouEnQue.print_structre()
        print('\nElimina los nodos')      
        newDouEnQue.pop_righ()
        newDouEnQue.print_structre()
        print('\n')
        newDouEnQue.pop_left()
        newDouEnQue.print_structre()

# Creando una Binary Tree
    def show_BinaryTree(self):
        Root = Node('Primer Nodo agregado')
        newBinaryTree = BinaryTree(Root)
        # newBinaryTree.print_structure() 
        
        print('\nAgregar Nodo a la derecha')     
        first_right_node = Node('Primer Nodo a la derecha')
        newBinaryTree.add_right(first_right_node)
        # newBinaryTree.print_structure()

        print('\nAgregar Nodo a la izquierda')     
        first_left_node = Node('Primer Nodo a la izquierda')
        newBinaryTree.add_left(first_left_node)
        newBinaryTree.print_structure()

        print('\nAgregar un nuevo Nodo a la derecha')
        second_right_node = Node('Segundo Nodo a la derecha')
        newBinaryTree.add_right(second_right_node)
        
        print('\nAgregar un nuevo Nodo a la izquierda')
        second_left_node = Node('Segundo Nodo a la izquierda')
        newBinaryTree.add_left(second_left_node)

        newBinaryTree.print_structure()


        print('\nAgregar un tercer Nodo a la derecha')
        third_right_node = Node('Tercer Nodo a la derecha')
        newBinaryTree.add_right(third_right_node)
        
        print('\nAgregar un tercer Nodo a la izquierda')
        third_left_node = Node('Tercer Nodo a la izquierda')
        newBinaryTree.add_left(third_left_node)

        newBinaryTree.print_structure()





