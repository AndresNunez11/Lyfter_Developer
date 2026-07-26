from nodoclass import Node

class Linkedlist:
    head: "Node"

    def __init__(self, head):
        self.head = head

    def insert_front(self, newnode):
        if(self.head is None):
            self.head =newnode
        else:
            auxnode = self.head
            self.head = newnode
            self.head.next = auxnode

    def insert_back(self, newnode):
        if(self.head is None):
            self.head =newnode
        else:
            currentNode = self.head
            while currentNode.next is not None:
                currentNode = currentNode.next
            currentNode.next = newnode

    def delet_data(self):
        if self.head:
            aux = self.head
            self.head = self.head.next   
        return aux

    def print_all(self):
        currentNode = self.head
        while currentNode is not None:
            print(f'{currentNode.data}')
            if currentNode.next is None:
                print('')
            else:
                print('->')
            currentNode = currentNode.next