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

stack = Stack()
print(stack.pop() is None)
stack.push(10)
print(stack.pop() == 10)
print(stack.pop() is None)
stack.push(10)
stack.push(11)
stack.push(12)
print(stack.pop() == 12)
print(stack.pop() == 11)
print(stack.peek() == 10)
print(stack.pop() == 10)
print(stack.pop() is None)


def is_balanced(string):
    right = []

    brackets = {
        '{': '}',
        '[': ']',
        '(': ')'
    }

    for letter in string:
        if brackets.get(letter):
            right.append(brackets[letter])
            continue

        if not right or right.pop() != letter:
            return "NO"

    if not right:
        return "YES"
    return "NO"

is_balanced('{[()]}')


