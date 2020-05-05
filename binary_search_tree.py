class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def __repr__(self):
        return str(self.data)


class BinaryTreeSearch:

    def __init__(self):
        self.tree = None

    def insert(self, data):
        node = Node(data=data)

        if not self.tree:
            self.tree = node
            return node

        return self._insert(self.tree, node)

    def _insert(self, node, new_node):
        if node.data < new_node.data:
            if not node.right:
                node.right = new_node
                return new_node
            return self._insert(node.right, new_node)
        if not node.left:
            node.left = new_node
            return new_node
        return self._insert(node.left, new_node)

    def printer(self):
        if not self.tree:
            print('[]')
        self._printer(self.tree)

    def _printer(self, node):
        if not node:
            return

        print(node.data)
        self._printer(node.left)
        self._printer(node.right)

    def height(self):
        if not self.tree:
            print('0')

        return self._height(self.tree)

    def _height(self, node):
        if not node:
            return -1

        return max(self._height(node.left), self._height(node.right)) + 1

    def lookup(self, data):
        if not self.tree:
            raise Exception(f'Not found {data}')

        self._lookup(self.tree, data)

    def _lookup(self, node, data):
        if node.data == data:
            return node

        if node.data < data:
            return self._lookup(node.right, data)
        else:
            return self._lookup(node.left, data)


tree = BinaryTreeSearch()
tree.height()
tree.printer()
tree.insert(10)
tree.insert(12)
tree.insert(14)
tree.insert(8)
tree.insert(9)
tree.insert(7)
tree.insert(3)
tree.printer()
tree.height()
tree.lookup(10)
tree.lookup(8)

