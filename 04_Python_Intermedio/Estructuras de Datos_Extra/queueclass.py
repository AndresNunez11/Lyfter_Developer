from nodoclass import Node

class Queue:
    head: "Node"

    def __init__(self, head):
        self.head = head

    def enqueue(self, newnode):
        if(self.head is None):
            self.head =newnode
        else:
            currentNode = self.head
            while currentNode.next is not None:
                currentNode = currentNode.next
            currentNode.next = newnode

    def dequeue(self):
        if self.head:
            aux = self.head
            self.head = self.head.next   
        return aux

    def print_all(self):
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