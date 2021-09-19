from collections import defaultdict


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


def breadth_first_search(root):

    if root is None:
        return

    queue = [root]
    while len(queue) > 0:
        item = queue.pop()

        if item.left:
            queue.append(item.left)

        if item.right:
            queue.append(item.right)


def breadth_first_search_with_value(root, search):

    if root is None:
        return

    queue = [root]
    while len(queue) > 0:
        item = queue.pop()

        if item.value == search:
            return item

        if item.left:
            queue.append(item.left)

        if item.right:
            queue.append(item.right)


def deep_first_search(root):

    if root is None:
        return

    deep_first_search(root.left)
    deep_first_search(root.right)


def deep_first_search_with_value(root, value):

    if root is None:
        return

    if root.value == value:
        return root

    return deep_first_search(root.left) or deep_first_search(root.right)


def findPath(root, path, k):
    if root is None:
        return False

    path.append(root.key)

    if root.key == k:
        return True

    if (
        (root.left and findPath(root.left, path, k)) or
        (root.right and findPath(root.right, path, k))
    ):
        return True

    path.pop()
    return False


def findLCA(root, value_1, value_2):
    path_1 = []
    path_2 = []


    if (not findPath(root, path_1, value_1) or
        not findPath(root, path_2, value_2)):
        return -1

    index = 0

    while(index < len(path_1) and index < len(path_2)):
        if path_1[index] != path_2[index]:
            break
        index += 1

    return path_1[index - 1]


def search_binary_tree(root, key):
    if not root or root.val == key:
        return root

    if root.val < key:
        return search_binary_tree(root.right, key)

    return search_binary_tree(root.left, key)


def insert_search_binary_tree(root, key):
    if not root:
        return Node(key)

    if root.val == key:
        return root

    elif root.val < key:
        root.right = search_binary_tree(
            root.right,
            key
        )
    else:
        root.left = search_binary_tree(
            root.left,
            key
        )
    return root


def merge_sort(items):
    if len(items) == 1:
        return items

    middle = len(items) // 2
    left = merge_sort(items[0:middle])
    rigth = merge_sort(items[middle:len(items)])

    index_left = 0
    index_rigth = 0
    items_sorted = []

    while (index_left < len(left) and index_rigth < len(rigth)):
        if left[index_left] < rigth[index_rigth]:
            items_sorted.append(left[index_left])
            index_left += 1
        else:
            items_sorted.append(rigth[index_rigth])
            index_rigth += 1

    while index_left < len(left):
        items_sorted.append(left[index_left])
        index_left += 1

    while index_rigth < len(rigth):
        items_sorted.append(rigth[index_rigth])
        index_rigth += 1

    return items_sorted


def quick_sort(array=[]):

    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return quick_sort(less) + equal + quick_sort(greater)
    else:
        return array


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def depth_first_search(self, value, visited=None):
        if not visited:
            visited = [False] * (max(self.graph) + 1)

        visited[value] = True
        print(value)

        for i in self.graph[value]:
            if not visited[i]:
                self.depth_first_search(i, visited)


