from nodoclass import Node
from queueclass import Queue

class BinaryTree:
    head: Node

    def __init__(self, head):
        self.head = head
    
    def print_structure(self):
        value = ''
        currentNode = self.head
        auxRight = currentNode.right
        auxLeft = currentNode.left
        i=0
        while currentNode is not None:
            # print(f'actual -> {currentNode.data}')  
            value +='\n'+str(currentNode.data)
            if(currentNode.right is not None):
                # print(f'Derecha ->{currentNode.right.data}')
                value+='->'+str(currentNode.right.data)
            else:
                # print('No hay datos a la derecha')
                value+='->'
            if(currentNode.left is not None):
                # print(f'Izquierda ->{currentNode.left.data}')
                value+='<-'+str(currentNode.left.data)
            else: 
                # print('No hay datos a la izquierda')
                value+='<-'
            if(auxRight == currentNode):
                # print(f'datos en el siguiente izquierda')
                currentNode = auxLeft
                if currentNode is None:
                    currentNode = None
                else:
                    if currentNode.right is None:
                        currentNode = None
                    else:
                        auxRight = currentNode.right
                        auxLeft = currentNode.left
            else:
                # print(f'datos en el siguiente derecha')
                if type(currentNode.right) == type(None):
                    currentNode = None
                else:
                    currentNode = currentNode.right     
            i+=1
        print(f'BinaryTree -> \n{value}')        




    # LLena primero el lado izquierdo del arbol, nceecsitaria mas metodos para controlar que parte del arbol voy a llenar
    def add_right(self, newnode):
        if self.head is None:
            self.head = newnode
        else:
            currentnode = self.head
            while currentnode.right is not None:
                # print('agrgando derecha')
                if currentnode.left is not None:
                    # print('Ya hay izquierdo')
                    currentnode = currentnode.left
                elif currentnode.right is not None:
                    # print('Ya hay derecho')
                    currentnode = currentnode.right               
            currentnode.right = newnode
    
    def add_left(self, newnode):
        if self.head is None:
            self.head = newnode
        else:
            currentnode = self.head
            while currentnode.left is not None:
                if currentnode.left is not None:
                    # print('Ya hay izquierdo')
                    currentnode = currentnode.left
                elif currentnode.right is not None:
                    # print('Ya hay derecho')
                    currentnode = currentnode.right 
            currentnode.left = newnode

    # returna una lista de los nodos que existen en el arbol para ser ordenados

    def binary_tree_list(self):
        queue = Queue(self.head)
        currentNode = self.head
        auxRight = currentNode.right
        auxLeft = currentNode.left
        currentNode = currentNode.right
        i=0
        while currentNode is not None:
            queue.enqueue(currentNode)
            if(auxRight == currentNode):
                currentNode = auxLeft
                if currentNode is None:
                    currentNode = None
                else:
                    if currentNode.right is None:
                        currentNode = None
                    else:
                        auxRight = currentNode.right
                        auxLeft = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode = None
                else:
                    currentNode = currentNode.right     
            i+=1
        return queue

