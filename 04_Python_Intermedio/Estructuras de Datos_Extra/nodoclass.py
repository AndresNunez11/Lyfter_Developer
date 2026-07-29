class Node:
    data: str
    next: "Node"  
    before: "Node"


    def __init__(self, data, next=None, before=None):
        self.data = data
        self.next = next
        self.before = before
    
    