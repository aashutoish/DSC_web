# 1. Write a program to show the implementation of Linked List in python.  
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None  # type: Node | None
        
class LinkList:
    def __init__(self):
        self.head = None
        
    def append(self, data):
        # Encapsulate the data in a Node 
        node = Node(data)
        if self.head is None:
            self.head = node    
        else: 
            current = self.head 
            while current.next:
                current = current.next 
            current.next = node 
            
if __name__ == "__main__":           
    words = LinkList()
    words.append('hello')
    words.append('world')
    words.append('bye')
    
    current = words.head
    while current:
        print(current.data)
        current = current.next
