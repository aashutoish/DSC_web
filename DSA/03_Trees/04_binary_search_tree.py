# 4. Write a program in python to implement Binary Search tree.  
class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self.insert_recursive(self.root, key)

    def insert_recursive(self, node, key):
        if not node:
            return BSTNode(key)
        if key < node.key:
            node.left = self.insert_recursive(node.left, key)
        elif key > node.key:
            node.right = self.insert_recursive(node.right, key)
        return node

    def search(self, key):
        return self.search_recursive(self.root, key)

    def search_recursive(self, node, key):
        if not node:
            return False
        if key == node.key:
            return True
        if key < node.key:
            return self.search_recursive(node.left, key)
        else:
            return self.search_recursive(node.right, key)

    def delete(self, key):
        self.root = self.delete_recursive(self.root, key)

    def delete_recursive(self, node, key):
        if not node:
            return None

        if key < node.key:
            node.left = self.delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self.delete_recursive(node.right, key)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            temp = self.min_value_node(node.right)
            node.key = temp.key
            node.right = self.delete_recursive(node.right, temp.key)

        return node

    def min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current


if __name__ == "__main__":
    bst = BinarySearchTree()
    elements = [50, 30, 20, 40, 70, 60, 80]
    print("Insert:", elements)
    for x in elements:
        bst.insert(x)

    print("Search 40:", bst.search(40))
    print("Search 90:", bst.search(90))

    print("Delete 20")
    bst.delete(20)
    print("Search 20:", bst.search(20))

    print("Delete 30")
    bst.delete(30)
    print("Search 30:", bst.search(30))
