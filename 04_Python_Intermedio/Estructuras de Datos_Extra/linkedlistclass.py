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
            auxnode.before = self.head
            self.head.next = auxnode


    def insert_back(self, newnode):
        if(self.head is None):
            self.head =newnode
        else:
            currentNode = self.head
            while currentNode.next is not None:
                currentNode = currentNode.next
            newnode.before = currentNode
            currentNode.next = newnode
            

    def delet_data(self, str):
        currentNode = self.head
        if(currentNode.data == str):
            self.head = currentNode.next
        else:
            while currentNode is not None:
                if(currentNode.data == str):
                    auxNode = currentNode #--B
                    beforeNode = auxNode.before #--A
                    currentNode = currentNode.next #--C
                    beforeNode.next = currentNode #--C
                    currentNode.before = beforeNode #--A
                else:
                    currentNode = currentNode.next 

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