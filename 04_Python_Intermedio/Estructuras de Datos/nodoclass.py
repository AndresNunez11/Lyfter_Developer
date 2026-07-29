class Node:
    data: str
    next: "Node"  
    right: "Node"
    left: "Node"  

    def __init__(self, data, next=None, right=None, left=None):
        self.data = data
        self.next = next
        self.right = right
        self.left = left        
    
    