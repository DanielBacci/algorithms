class Node:

    def __init__(self, value, node_next):
        self.value = value
        self.node_next = node_next


class Stack:

    def __init__(self):
        self.top = None
        self.bottom = None
        self.lenght = 0

    def pop(self):
        node = self.top
        if not node:
            return None

        self.top = node.node_next
        if not self.top:
            self.bottom = None

        self.lenght -= 1
        return node.value

    def push(self, value):
        node = Node(value, self.top)
        self.top = node

        if not self.bottom:
            self.bottom = node

        self.lenght += 1

    def peek(self):
        if self.top:
            return self.top.value
        return None


class Queue:

    def __init__(self):
        self.queue_1 = Stack()
        self.queue_2 = Stack()
        self.lenght = 0

    def pop(self):
        if self.lenght == 0:
            return None

        self.lenght -= 1

        return self.queue_1.pop()

    def push(self, value):
        while self.queue_1.lenght != 0:
            self.queue_2.push(
                self.queue_1.pop()
            )

        self.queue_1.push(value)

        while self.queue_2.lenght != 0:
            self.queue_1.push(
                self.queue_2.pop()
            )

        self.lenght += 1

    def peek(self):
        return self.queue_1.peek()


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
