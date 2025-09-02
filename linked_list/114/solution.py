# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def flatter_recursion(self, root):
        """
        root.val = 6
        root.left.value = 44
        root.right.value = [23, 70] 
        """
        if not root:
            return None

        if not root.left and not root.right:
            return root
        
        left_tail = self.flatter_recursion(root.left) 
        right_tail = self.flatter_recursion(root.right)

        if left_tail:
            left_tail.right = root.right
            root.right = root.left
            root.left = None
        
        return right_tail or left_tail


    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.flatter_recursion(root)
        
