from nodoclass import Node

class Stack:
    head: Node

    def __init__(self, head):
        self.head = head
    
    def print_structre(self):
        value = ''
        currentNode = self.head
        while currentNode is not None:
            if currentNode.next is not None:
                value += str(currentNode.data)+'->'
            else:
                value += str(currentNode.data)
            currentNode = currentNode.next
        print(f'Stack -> {value}')

    def push_stack(self, newnode):
        auxnode = self.head
        self.head = newnode
        self.head.next = auxnode

    def pop_stack(self):
        if self.head:
            self.head = self.head.next
