from nodoclass import Node

class Stack:
    head: Node

    def __init__(self, head):
        self.head = head
    
    def print_structre(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.data)
            currentNode = currentNode.next

    def push_stack(self, newnode):
        auxnode = self.head
        self.head = newnode
        self.head.next = auxnode

    def pop_stack(self):
        if self.head:
            self.head = self.head.next
