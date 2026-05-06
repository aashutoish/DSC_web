# 2. Write the implementation of Singly Linked Lists to show creation, traversal, insertion, 
# retrieval and deletion of elements.  
class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None  # type: Node | None
    def __repr__(self):
        return str(self.data)
    
class SingleyLinkedlist:
    def __init__(self):
        self.head = None #Pointer to the first node 
        self.tail = None #Pointer to the last node 
        self.count = 0 #Tracks the number of nodes
     
    def is_empty(self):
        return self.head is None
    
    def __len__(self):
        return self.count
    
    def __repr__(self):
        nodes = []
        current = self.head 
        while current:
            nodes.append(str(current.data))
            current = current.next
        return "->".join(nodes)+"-> None"
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        self.count +=1
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            
    def insert_at_end(self,data):
        new_node = Node(data)
        self.count +=1 
        
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            if self.tail:
                self.tail.next = new_node
            self.tail = new_node
    
    def insert_after_node(self,prev_node,data):
        if not prev_node:
            print("Error: Previous node is None.")
            return 
        
        #Handle if prev_node is the tail
        if prev_node == self.tail:
            self.insert_at_end(data)
            return
        new_node =Node(data)
        new_node.next = prev_node.next 
        prev_node.next = new_node
        self.count +=1
    
    def delete_at_beginning(self):
        if self.is_empty():
            print("Error:List is empty.") 
            return None
        
        self.count -=1
        node_to_delete = self.head
        
        #List has only one node 
        if self.head == self.tail:
            self.head = None
            self.tail = None 
        else:
            if self.head:
                self.head = self.head.next 
            
        return node_to_delete
             
    def delete_at_end(self):
        if self.is_empty():
            print("Error:List is empty.")
            return None
        
        self.count -=1
        
        #If only one node 
        if self.head == self.tail:
            if self.head:
                node_data = self.head.data
            self.head = None
            self.tail = None
            return node_data
        
        #Traverse to find the second-to-last node
        prev = self.head
        if prev:
            while prev.next and prev.next != self.tail:
                prev = prev.next
            
        if self.tail:
            node_data = self.tail.data
        if prev:
            prev.next = None 
        self.tail = prev #Update the tail pointer 
            
        return node_data
    
    def delete_by_key(self,key):
        if self.is_empty():
            print('Error:List is empty')
            return
        
        #If head node holds the key
        if self.head and self.head.data == key:
            self.delete_at_beginning()
            return 
        #Traverse to find the key
        prev = self.head
        current = self.head.next if self.head else None
        
        while current:
            if current.data == key:
                if prev:
                    prev.next = current.next
                if current == self.tail: #Check if we're deleting the tail
                    self.tail = prev
                self.count -=1
                return 
            prev = current 
            current = current.next     

        
        print(f"Error:Key '{key}' not found in list.")
        
    def traverse(self):
        print("SLL:",end=" ")
        current = self.head
        while current:
            print(current.data, end ="->")
            current = current.next
        print("None")
        
    def search(self,key):
        current = self.head
        while current:
            if current.data == key:
                return current 
            current = current.next
        return None #key not found 

if __name__ == "__main__":
    sll = SingleyLinkedlist()
    sll.insert_at_beginning(20)
    print(sll)
    sll.insert_at_end(7)
    print(sll)
    sll.insert_at_end(9)
    print(sll)
    sll.insert_at_end(13)
    print(sll)
    sll.delete_at_beginning()
    print(sll)
    sll.delete_at_end()
    print(sll)
