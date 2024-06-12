class Node:
    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None

class Tree:
    def __init__(self, value=None):
        self.nodes = []
        self.value = value
        self.left = None
        self.right = None
        self.root = None

    def append(self, node):
        self.nodes.append(node)

    def __len__(self):
        return len(self.nodes)

    def __getitem__(self, index):
        return self.nodes[index]

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, node):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(value, node.left)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(value, node.right)
        else:
            print("Value already in tree")