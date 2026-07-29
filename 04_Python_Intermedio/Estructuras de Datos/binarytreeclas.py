from nodoclass import Node

class BinaryTree:
    head: Node

    def __init__(self, head):
        self.head = head
    
    def print_structure(self):
        currentNode = self.head
        auxRight = currentNode.right
        auxLeft = currentNode.left
        i=0
        while currentNode is not None:
            print(f'\nCliclo -- {i}')
            print(f'actual -> {currentNode.data}')   
            if(currentNode.right is not None):
                print(f'Derecha ->{currentNode.right.data}')
            else:
                print('No hay datos a la derecha')
            if(currentNode.left is not None):
                print(f'Izquierda ->{currentNode.left.data}')
            else: 
                print('No hay datos a la izquierda')
            if(auxRight == currentNode):
                # if auxRight is not None or auxLeft is not None:
                #     print(f'Auxiliar en el if {auxRight.data}')
                #     print(f'Auxiliar en el if {auxLeft.data}')              
                # else:
                #     print('no hay datos en auxiliar izquierdo en el if') 
                # print(f'Actual en el if {currentNode.data}')
                currentNode = auxLeft
                auxRight = currentNode.right
                auxLeft = currentNode.left
            else:
                # if auxRight is not None or auxLeft is not None:
                #     print(f'Auxiliar en el else {auxRight.data}')
                #     print(f'Auxiliar en el else {auxLeft.data}') 
                # else: 
                #     print('no hay datos en auxiliar derecho en el else') 
                # print(f'Actual en el else {currentNode.data}')
                currentNode = currentNode.right
            i+=1
                
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

