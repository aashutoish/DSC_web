# 1. Write a program to implement tree data structure in python. User must be able to insert 
# and retrieve data from tree.  
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []  # list of child nodes

    def add_child(self, child_node):
        self.children.append(child_node)

    def __repr__(self):
        return f"TreeNode({self.value})"


class Tree:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)

    def find(self, node, value):
        if node.value == value:
            return node
        for child in node.children:
            found = self.find(child, value)
            if found:
                return found
        return None

    def display(self, node, level=0):
        print(" " * level * 2 + str(node.value))
        for child in node.children:
            self.display(child, level + 1)


if __name__ == "__main__":
    tree = Tree("Root")

    child1 = TreeNode("Child1")
    child2 = TreeNode("Child2")
    tree.root.add_child(child1)
    tree.root.add_child(child2)

    child1.add_child(TreeNode("Grandchild1"))
    child1.add_child(TreeNode("Grandchild2"))
    child2.add_child(TreeNode("Grandchild3"))

    print("Tree Structure:")
    tree.display(tree.root)

    search_value = "Grandchild2"
    found_node = tree.find(tree.root, search_value)
    print(f"\nSearching for '{search_value}':", "Found!" if found_node else "Not Found")
