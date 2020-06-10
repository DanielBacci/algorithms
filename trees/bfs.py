from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)
        self.length = 0

    def addEdge(self, key, value):
        self.graph[key].append(value)
        self.length += 1

    def breadth_first_search(self, value):
        visited = [False] * self.length

        queue = []
        queue.append(value)
        visited[value] = True

        while queue:
            value = queue.pop(0)
            print(value)
            for index in self.graph[value]:
                if not visited[index]:
                    queue.append(index)
                    visited[index] = True


graph = Graph()
graph.addEdge(0, 1)
graph.addEdge(0, 2)
graph.addEdge(1, 2)
graph.addEdge(2, 0)
graph.addEdge(2, 3)
graph.addEdge(3, 3)
graph.breadth_first_search(2)
