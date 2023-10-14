class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            self._insert_rec(self.root, key)

    def _insert_rec(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_rec(node.left, key)
        elif key > node.key:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_rec(node.right, key)

    def extract_min(self):
        if self.root is None:
            return None

        min_node = self._find_min(self.root)
        self.root = self._delete(self.root, min_node.key)
        return min_node

    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def _delete(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            min_node = self._find_min(node.right)
            node.key = min_node.key
            node.right = self._delete(node.right, min_node.key)

        return node

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None