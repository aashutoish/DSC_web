# 2. Implement BFS for value retrieval from tree in python. 
from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None  # type: TreeNode | None
        self.right = None  # type: TreeNode | None

class BFSTraversal:
    @staticmethod
    def level_order(root):
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            current = queue.popleft()
            result.append(current.value)

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        return result


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)

    print("BFS Level Order:", BFSTraversal.level_order(root))
