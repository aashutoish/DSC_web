# 5. Implement AVL Tree in python.

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None  # type: Node | None
        self.right = None  # type: Node | None
        self.height = 1


class AVLTree:
    def height(self, node):
        if node is None:
            return 0
        return node.height

    def balance(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def right_rotate(self, node):
        left_node = node.left
        temp = left_node.right

        left_node.right = node
        node.left = temp

        node.height = 1 + max(self.height(node.left), self.height(node.right))
        left_node.height = 1 + max(self.height(left_node.left), self.height(left_node.right))

        return left_node

    def left_rotate(self, node):
        right_node = node.right
        temp = right_node.left

        right_node.left = node
        node.right = temp

        node.height = 1 + max(self.height(node.left), self.height(node.right))
        right_node.height = 1 + max(self.height(right_node.left), self.height(right_node.right))

        return right_node

    def insert(self, root, key):
        if root is None:
            return Node(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        diff = self.balance(root)

        if diff > 1 and root.left and key < root.left.key:
            return self.right_rotate(root)

        if diff < -1 and root.right and key > root.right.key:
            return self.left_rotate(root)

        if diff > 1 and root.left and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if diff < -1 and root.right and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root


if __name__ == "__main__":
    tree = AVLTree()
    root = None

    numbers = [10, 20, 30, 40, 50, 25]
    print("Insert:", numbers)

    for num in numbers:
        root = tree.insert(root, num)

    if root:
        print("Root:", root.key)
        print("Height:", root.height)
        if root.left:
            print("Left child:", root.left.key)
        if root.right:
            print("Right child:", root.right.key)
