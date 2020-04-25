class Node:

    def __init__(self, value, node_next):
        self.value = value
        self.node_next = node_next


class Queue:

    def __init__(self):
        self.first = None
        self.last = None
        self.lenght = 0

    def pop(self):
        node = self.first
        if not node:
            return None

        self.first = node.node_next
        if not self.first:
            self.last = None

        self.lenght -= 1
        return node.value

    def push(self, value):
        node = Node(value, None)

        if self.last:
            self.last.node_next = node
        self.last = node

        if not self.first:
            self.first = node

        self.lenght += 1

    def peek(self):
        if self.first:
            return self.first.value
        return None

queue = Queue()
print(queue.pop() is None)
queue.push(10)
print(queue.pop() == 10)
print(queue.pop() is None)
queue.push(10)
queue.push(11)
queue.push(12)
print(queue.pop() == 10)
print(queue.pop() == 11)
print(queue.peek() == 12)
print(queue.pop() == 12)
print(queue.pop() is None)
