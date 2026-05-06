# 3. Write a program to implement the Doubly Linked List. 
class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None  # type: DNode | None
        self.prev = None  # type: DNode | None

    def __repr__(self):
        return str(self.data)


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

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
        return " <-> ".join(nodes) if nodes else "Empty List"

    def traverse(self):
        print("DLL (Forward):", end=" ")
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def traverse_reverse(self):
        print("DLL (Reverse):", end=" ")
        current = self.tail
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")

    def insert_at_beginning(self, data):
        new_node = DNode(data)
        self.count += 1

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = DNode(data)
        self.count += 1

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            if self.tail:
                self.tail.next = new_node
            self.tail = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Error: Previous node is None.")
            return

        if prev_node == self.tail:
            self.insert_at_end(data)
            return

        new_node = DNode(data)
        new_node.next = prev_node.next
        new_node.prev = prev_node
        prev_node.next.prev = new_node
        prev_node.next = new_node
        self.count += 1

    def delete_at_beginning(self):
        if self.is_empty():
            print("Error: List is empty.")
            return None

        node_to_delete = self.head
        self.count -= 1

        if self.head == self.tail:  # Only one node
            self.head = None
            self.tail = None
        else:
            if self.head:
                self.head = self.head.next
            if self.head:
                self.head.prev = None

        return node_to_delete.data if node_to_delete else None

    def delete_at_end(self):
        if self.is_empty():
            print("Error: List is empty.")
            return None

        node_to_delete = self.tail
        self.count -= 1

        if self.head == self.tail:  # Only one node
            self.head = None
            self.tail = None
        else:
            if self.tail:
                self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None

        return node_to_delete.data if node_to_delete else None

    def delete_by_key(self, key):
        current = self.head

        while current:
            if current.data == key:
                data = current.data
                self.count -= 1

                if current == self.head:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                    else:
                        self.tail = None
                elif current == self.tail:
                    self.tail = current.prev
                    if self.tail:
                        self.tail.next = None
                else:
                    if current.prev:
                        current.prev.next = current.next
                    if current.next:
                        current.next.prev = current.prev

                return data
            current = current.next

        print(f"Error: key '{key}' not found in list")
        return None


# Example usage
if __name__ == "__main__":
    dll = DoublyLinkedList()

    # Insert at beginning and end
    dll.insert_at_beginning(10)
    dll.insert_at_end(20)
    dll.insert_at_end(30)
    dll.insert_at_beginning(5)

    dll.traverse()
    dll.traverse_reverse()

    # Insert after a node
    if dll.head and dll.head.next:
        dll.insert_after_node(dll.head.next, 15)  # Insert after 10
    dll.traverse()

    # Delete operations
    print("Deleted from beginning:", dll.delete_at_beginning())
    dll.traverse()

    print("Deleted from end:", dll.delete_at_end())
    dll.traverse()

    print("Deleted by key (15):", dll.delete_by_key(15))
    dll.traverse()
