###
When to use Pre-Order, In-order or Post-Order?
The traversal strategy the programmer selects depends on the specific needs of the algorithm being designed. The goal is speed, so pick the strategy that brings you the nodes you require the fastest.

If you know you need to explore the roots before inspecting any leaves, you pick pre-order because you will encounter all the roots before all of the leaves.

If you know you need to explore all the leaves before any nodes, you select post-order because you don't waste any time inspecting roots in search for leaves.

If you know that the tree has an inherent sequence in the nodes, and you want to flatten the tree back into its original sequence, than an in-order traversal should be used. The tree would be flattened in the same way it was created. A pre-order or post-order traversal might not unwind the tree back into the sequence which was used to create it.

https://stackoverflow.com/questions/9456937/when-to-use-preorder-postorder-and-inorder-binary-search-tree-traversal-strate
###

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
