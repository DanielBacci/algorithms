# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def tree_linked_list(self, node):
        if not node:
            return node

        if not node.left and not node.right:
            return node

        most_left = self.tree_linked_list(node.left)
        most_right = self.tree_linked_list(node.right)

        if most_left:
            most_left.right = node.right
            node.right = node.left
            node.left = None

        return most_right or most_left


    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.tree_linked_list(root)
        
