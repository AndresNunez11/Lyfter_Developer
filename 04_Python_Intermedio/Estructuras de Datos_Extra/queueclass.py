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
        while currentNode is not None:
            print(f'{currentNode.data}')
            if(currentNode.next is not None):
                print(f'->')
            else:
                print(f'-> No hay siguiente')
            currentNode = currentNode.next