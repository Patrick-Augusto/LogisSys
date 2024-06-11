class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, caminhao):
        if self.root is None:
            self.root = TreeNode(caminhao)
        else:
            self._insert(caminhao, self.root)

    def _insert(self, caminhao, node):
        if caminhao < node.val:
            if node.left is None:
                node.left = TreeNode(caminhao)
            else:
                self._insert(caminhao, node.left)
        else:
            if node.right is None:
                node.right = TreeNode(caminhao)
            else:
                self._insert(caminhao, node.right)