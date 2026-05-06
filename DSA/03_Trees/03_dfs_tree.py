# 3. Implement DFS for value retrieval from tree in python.
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None  # type: TreeNode | None
        self.right = None  # type: TreeNode | None

class DFSTraversal:
    @staticmethod
    def preorder(node):
        if not node:
            return []
        return [node.value] + DFSTraversal.preorder(node.left) + DFSTraversal.preorder(node.right)

    @staticmethod
    def inorder(node):
        if not node:
            return []
        return DFSTraversal.inorder(node.left) + [node.value] + DFSTraversal.inorder(node.right)

    @staticmethod
    def postorder(node):
        if not node:
            return []
        return DFSTraversal.postorder(node.left) + DFSTraversal.postorder(node.right) + [node.value]


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)

    print("DFS Preorder:", DFSTraversal.preorder(root))
    print("DFS Inorder:", DFSTraversal.inorder(root))
    print("DFS Postorder:", DFSTraversal.postorder(root))
