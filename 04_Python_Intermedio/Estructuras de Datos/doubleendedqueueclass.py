from nodoclass import Node

class DoubleEndedQueue:
    head: Node
    tail: Node

    def __init__(self, head):
        self.head = head
        self.tail = None
    
    def print_structre(self):
        currentNode = self.head
        while currentNode is not None:
            if type(currentNode.next) == type(None):
                self.tail = currentNode
                currentNode =None
            else:                
                currentNode = currentNode.next
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.data)
            currentNode = currentNode.next

    def push_right(self, newnode):
        auxnode = self.head
        self.head = newnode
        self.head.next = auxnode
    
    def push_left(self, newnode):
        currentNode = self.head
        self.tail = newnode
        while currentNode.next is not None:
            currentNode = currentNode.next
        # print(self.head.data)
        # print(currentNode.data)
        # print(self.tail.data)
        currentNode.next = self.tail
        # print(currentNode.next.data)
        # print(self.tail.data)


    def pop_righ(self):
        if self.head:
            self.head = self.head.next

    def pop_left(self):
        currentNode = self.head
        # print(self.tail.data)
        # print('Debe eliminar el nodo de la izquierda')
        while currentNode.next is not None:
            currentNode = currentNode.next
            if currentNode.next == self.tail:
                currentNode.next = None
                self.tail = currentNode
        