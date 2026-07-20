from nodoclass import Node

class Queue:
    head: Node

    def __init__(self, head):
        self.head = head
    
    def print_structre(self):
        currentNode = self.head
        while currentNode is not None:
            print(f'actual -> {currentNode.data}')
            if(currentNode.next is not None):
                print(f'siguiente ->{currentNode.next.data}\n')
            else:
                print(f'No hay siguiente')
            currentNode = currentNode.next
    
    def enqueue(self, newnode):
        currentNode = self.head
        while currentNode.next is not None:
            currentNode = currentNode.next
        # print(currentNode.data)
        # print(self.head.data)
        currentNode.next = newnode
    

    def dequeue(self):
        if self.head:
            self.head = self.head.next
