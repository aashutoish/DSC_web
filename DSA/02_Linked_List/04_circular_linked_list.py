# 4. Circular Linked List - stores data cyclically

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # type: Node | None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            current = self.head
            while current.next and current.next != self.head:
                current = current.next
            if current:
                current.next = new_node
            new_node.next = self.head

    def display(self):
        if not self.head:
            print("Empty list")
            return
        current = self.head
        while True:
            if current:
                print(current.data, end=" -> ")
                current = current.next
            if current == self.head:
                print("(back to head)")
                break

if __name__ == "__main__":
    cll = CircularLinkedList()
    cll.append(10)
    cll.append(20)
    cll.append(30)
    cll.display()
