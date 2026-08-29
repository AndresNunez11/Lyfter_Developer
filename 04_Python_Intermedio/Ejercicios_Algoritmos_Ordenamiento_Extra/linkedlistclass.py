from nodoclass import Node

class LinkedList:
    head: Node

    def __init__(self, head):
        self.head = head
        self.value = ''
    
    def print_structre(self):
        self.value = ''
        currentNode = self.head
        while currentNode is not None:
            if currentNode.next is None:
                self.value = self.value +str(currentNode.data) 
            else: 
                self.value = self.value +str(currentNode.data) + '-> ' 
            # print(currentNode.data)
            currentNode = currentNode.next
        print(f'Linked list -> {self.value}')

