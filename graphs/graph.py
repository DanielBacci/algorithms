class Graph:

    def __init__(self):
        self.length = 0
        self.nodes = {}

    def add_node(self, node):
        self.nodes[node] = []
        self.length += 1

    def add_vertex(self, node_1, node_2):
        self.nodes[node_1].append(node_1)
        self.nodes[node_1].append(node_2)
