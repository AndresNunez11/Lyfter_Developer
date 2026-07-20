from nodoclass import Node

class LinkedList:
    head: Node

    def __init__(self, head):
        self.head = head
    
    def print_structre(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.data)
            currentNode = currentNode.next
