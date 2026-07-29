from nodoclass import Node

class DoubleList:
    head: "Node"
    tail: "Node"

    def __init__(self, head):
        self.head = head
        self.tail = head
        # self.head.next = self.tail
        # self.tail.before = self.head

    def append(self, newnode):
        if(self.head is None):
            self.head =newnode
            self.tail =newnode
        else: 
            currentNode = self.head
            while currentNode.next is not None:
                auxNode = currentNode
                currentNode = currentNode.next
                currentNode.before = auxNode
            AuxNode = newnode
            AuxNode.before = currentNode
            currentNode.next = AuxNode
            self.tail = currentNode.next
    
    def prepend(self, newnode):
        if(self.head is None):
            self.head =newnode
            self.tail =newnode
        else:
            auxNode = self.head
            self.head = newnode
            auxNode.before = self.head
            self.head.next = auxNode
    
    def delete_data(self,str):
        currentNode = self.head
        if(currentNode.data == str):
            self.head = currentNode.next
        else:
            while currentNode is not None:
                if currentNode.data == str:
                    auxNode = currentNode #--B
                    beforeNode = auxNode.before #--A
                    # nextnode = auxNode.next #--C
                    currentNode = currentNode.next #--C
                    beforeNode.next = currentNode #--C
                    currentNode.before = beforeNode #--A
                    # return auxNode
                else:
                    currentNode = currentNode.next
        # return Node(f'Dato {str} no esta en la lista') # deberia de manejarse como un error 
        

    def print_forward(self):
        currentNode = self.head
        aux = ''
        while currentNode is not None:
            str = currentNode.data 
            aux= aux+str
            if currentNode.next is not None:
                aux= aux+'-> '
            else:
                aux =aux 
            currentNode = currentNode.next
        print(f'{aux}')


    
    def print_backward(self):
        currentNode = self.tail
        aux = ''
        while currentNode is not None:
            str = currentNode.data 
            aux= aux+str
            if currentNode.before is not None:
                aux= aux+'-> '
            else:
                aux =aux 
            currentNode = currentNode.before
        print(f'{aux}')
        
