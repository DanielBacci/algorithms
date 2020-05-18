from collections import defaultdict


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


graph = Graph()
graph.addEdge(0, 1)
graph.addEdge(0, 2)
graph.addEdge(1, 2)
graph.addEdge(2, 0)
graph.addEdge(2, 3)
graph.addEdge(3, 3)

graph.depth_first_search(2)
