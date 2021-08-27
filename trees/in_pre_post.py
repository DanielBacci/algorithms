class Node:

    def __init__(
        self, data, right, left
    ):
        self.data = data
        self.right = right
        self.left = left

    def in_order(self, node):
        if not node:
            return None

        self.in_order(self.left)
        print(self.data)
        self.in_order(self.right)


    def pre_order(self, node):
        if not node:
            return None

        print(self.data)
        self.pre_order(self.left)
        self.pre_order(self.right)


    def post_order(self, node):
        if not node:
            return None

        self.post_order(self.left)
        self.post_order(self.right)
        print(self.data)
