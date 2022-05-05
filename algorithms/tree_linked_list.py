def linked_list(self, node):

	if node == None or 
	   node.left is None and node.right is None:
	   return

	if node.left != None:
		linked_list(node.left)

		right_none = node.right
		node.right = node.left
		node.left = None

		right = node.right
		while right.right is not None:
			right = right.right

		right.right = right_none


	linked_list(node.right)
