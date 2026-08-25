from inidataclass import Datos
from nodoclass import Node
from linkedlistclass import LinkedList
from queueclass import Queue
from stackclass import Stack
from doubleendedqueueclass import DoubleEndedQueue
from binarytreeclas import BinaryTree
from bubblesortclass import BubbleSort
from sortexerciseclass import bubble_sort, bubble_sort_steps, validated_bubble_sort


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
        firts_node = Node(5)
        second_node = Node(1)
        third_node = Node(3)
        fourth_node = Node(2)
        fith_node = Node(4)
        empty_node = None        
        firts_node.next = second_node
        second_node.next = third_node
        third_node.next = fourth_node
        fourth_node.next = fith_node
        # linked_list = LinkedList(self.firts_node)
        linked_list = LinkedList(empty_node)
        linked_list.print_structre()
        linked_bubblesort = BubbleSort(linked_list)
        linked_bubblesort.bubble_sort_linkedlist()
        # aux_list = BubbleSort(firts_node)
        # print(aux_list.bubble_sort_list())
        # print('Metodo Bubble sort')
        # # print(f'{aux_list.bubble_sort_list()}')
        # linked_list = BubbleSort.bubble_sort_list(linked_list)

# Creando una cola queue
    def show_queue(self):
        firts_node = Node(5)
        second_node = Node(1)
        third_node = Node(3)
        fourth_node = Node(2)
        fith_node = Node(4)
        sixth_node= Node(8)
        seventh_node= Node(6)
        eight_node= Node(7)
        # empty_node = None
        # firts_node = Node('Soy el primer nodo')
        # second_node = Node('Soy el segundo nodo')
        # third_node = Node('Soy el tercer nodo')
        firts_node.next = second_node
        second_node.next = third_node
        third_node.next = fourth_node
        fourth_node.next = fith_node
        fith_node.next = sixth_node
        sixth_node.next = seventh_node
        seventh_node.next = eight_node
        new_node = Node('A')
        newQueue =  Queue(firts_node)
        newQueue.enqueue(new_node)
        newQueue.print_structre()
        linked_bubblesort = BubbleSort(newQueue)
        linked_bubblesort.bubble_sort_linkedlist()

        # print('--Dequeue--')
        # newQueque.dequeue()
        # newQueque.print_structre()
        # print('--Enqueue--')
        # fourth_node = Node('Soy el cuarto nodo')
        # newQueque.enqueue(fourth_node)
        # newQueque.print_structre()
    
# Creando una cola stack
    def show_stack(self):
        firts_node = Node(5)
        second_node = Node(1)
        third_node = Node(3)
        fourth_node = Node(2)
        fith_node = Node(4)
        sixth_node= Node(8)
        seventh_node= Node(6)
        eight_node= Node(7)
        empty_node = None

        firts_node.next = second_node
        second_node.next = third_node
        newStack=  Stack(firts_node)
        newStack.push_stack(fourth_node)
        newStack.push_stack(fith_node)
        newStack.push_stack(sixth_node)
        newStack.push_stack(seventh_node)
        newStack.push_stack(eight_node)
        newStack.print_structre()
        linked_bubblesort = BubbleSort(newStack)
        linked_bubblesort.bubble_sort_linkedlist()

# Creando una cola Double ended Queue
    def show_DobleEndedQueue(self):
        firts_node = Node(5)
        second_node = Node(1)
        third_node = Node(3)
        fourth_node = Node(2)
        fith_node = Node(4)
        sixth_node= Node(8)
        seventh_node= Node(6)
        eight_node= Node(7)
        empty_node = None
        firts_node.next = second_node
        newDouEnQue = DoubleEndedQueue(firts_node)
        newDouEnQue.push_right(third_node)
        newDouEnQue.push_left(fourth_node)
        newDouEnQue.push_right(fith_node)
        newDouEnQue.push_left(sixth_node)
        newDouEnQue.push_right(seventh_node)
        newDouEnQue.push_left(eight_node)
        newDouEnQue.print_structre()
        linked_bubblesort = BubbleSort(newDouEnQue)
        linked_bubblesort.bubble_sort_linkedlist()

# Creando una Binary Tree
    def show_BinaryTree(self):
        firts_node = Node(5)
        second_node = Node(1)
        third_node = Node(3)
        fourth_node = Node(2)
        fith_node = Node(4)
        sixth_node= Node(8)
        seventh_node= Node(6)
        eight_node= Node(7)
        empty_node = None
        Root = firts_node
        newBinaryTree = BinaryTree(Root)
        newBinaryTree.add_right(second_node)
        newBinaryTree.add_left(third_node)
        newBinaryTree.add_right(fourth_node)
        newBinaryTree.add_left(fith_node)
        newBinaryTree.add_right(sixth_node)
        newBinaryTree.add_left(seventh_node)
        newBinaryTree.add_right(eight_node)        
        newBinaryTree.print_structure()
        linked_bubblesort = BubbleSort(newBinaryTree.binary_tree_list())
        linked_bubblesort.bubble_sort_linkedlist()

    def sortexercise(self):
        numberlist1 = [5,3,8,1,2]
        print(f'Lista original: \n{numberlist1}')
        print(f'Lista Ordenada:\n{bubble_sort(numberlist1)}')
        result = bubble_sort_steps(numberlist1)
        print("Lista ordenada:", result[0])
        print("Iteraciones:", result[1])
        print("Comparaciones:", result[2])
        # numberlist2 = [5,'Hola',2]
        # print(f'{validated_bubble_sort(numberlist2)}')
        numberlist3 = []
        print(f'{validated_bubble_sort(numberlist3)}')







