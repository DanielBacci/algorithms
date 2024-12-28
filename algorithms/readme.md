### Graph Algorithms with Python Implementations

Below is a detailed explanation and Python implementation of common graph algorithms, including when to use each and how they work.

---

### 1. **Breadth-First Search (BFS)**

#### **When to Use:**
- Find the shortest path in unweighted graphs.
- Determine connectivity or discover levels in a graph.

#### **How It Works:**
BFS explores neighbors layer by layer using a queue.

```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    while queue:
        node = queue.popleft()
        print(node, end=" ")  # Process node
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Example Usage
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1],
    5: [2]
}
bfs(graph, 0)  # Output: 0 1 2 3 4 5
```

---

### 2. **Depth-First Search (DFS)**

#### **When to Use:**
- Detect cycles.
- Find paths or check connectivity.

#### **How It Works:**
DFS explores as far as possible before backtracking using recursion or a stack.

```python
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")  # Process node
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example Usage
dfs(graph, 0)  # Output: 0 1 3 4 2 5
```

---

### 3. **Dijkstra's Algorithm**

#### **When to Use:**
- Find the shortest path in graphs with non-negative weights.

#### **How It Works:**
Uses a priority queue to explore nodes with the smallest cumulative distance.

```python
import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]  # (distance, node)
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

# Example Usage
graph = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: []
}
print(dijkstra(graph, 0))  # Output: {0: 0, 1: 3, 2: 1, 3: 4}
```

---

### 4. **Bellman-Ford Algorithm**

#### **When to Use:**
- Find shortest paths in graphs with negative weights.
- Detect negative weight cycles.

#### **How It Works:**
Iteratively relax all edges up to \( V - 1 \) times.

```python
def bellman_ford(graph, vertices, start):
    distances = {v: float('inf') for v in range(vertices)}
    distances[start] = 0

    for _ in range(vertices - 1):
        for u, v, weight in graph:
            if distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
    
    # Check for negative weight cycles
    for u, v, weight in graph:
        if distances[u] + weight < distances[v]:
            return "Negative weight cycle detected"
    
    return distances

# Example Usage
graph = [
    (0, 1, 4),
    (0, 2, 1),
    (2, 1, 2),
    (1, 3, 1),
    (2, 3, 5)
]
print(bellman_ford(graph, 4, 0))  # Output: {0: 0, 1: 3, 2: 1, 3: 4}
```

---

### 5. **Floyd-Warshall Algorithm**

#### **When to Use:**
- Find shortest paths between all pairs of vertices.

#### **How It Works:**
Dynamic programming approach that updates paths iteratively.

```python
def floyd_warshall(graph, vertices):
    distance = [[float('inf')] * vertices for _ in range(vertices)]
    
    for u, v, weight in graph:
        distance[u][v] = weight
    for i in range(vertices):
        distance[i][i] = 0
    
    for k in range(vertices):
        for i in range(vertices):
            for j in range(vertices):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    
    return distance

# Example Usage
graph = [
    (0, 1, 4),
    (0, 2, 1),
    (2, 1, 2),
    (1, 3, 1),
    (2, 3, 5)
]
print(floyd_warshall(graph, 4))
```

---

### 6. **Prim's Algorithm**

#### **When to Use:**
- Find the Minimum Spanning Tree (MST) in a graph.

#### **How It Works:**
Expands the MST by adding the smallest edge connecting to a new vertex.

```python
import heapq

def prim(graph, vertices):
    visited = set()
    pq = [(0, 0)]  # (weight, node)
    mst_cost = 0
    
    while pq and len(visited) < vertices:
        weight, u = heapq.heappop(pq)
        if u in visited:
            continue
        visited.add(u)
        mst_cost += weight
        for v, w in graph[u]:
            if v not in visited:
                heapq.heappush(pq, (w, v))
    
    return mst_cost

# Example Usage
graph = {
    0: [(1, 4), (2, 1)],
    1: [(0, 4), (2, 2), (3, 5)],
    2: [(0, 1), (1, 2), (3, 8)],
    3: [(1, 5), (2, 8)]
}
print(prim(graph, 4))  # Output: 7
```

---

### 7. **Kruskal's Algorithm**

#### **When to Use:**
- Find the MST using edge weights.

#### **How It Works:**
Sorts edges by weight and uses union-find to avoid cycles.

```python
def kruskal(edges, vertices):
    edges.sort(key=lambda x: x[2])  # Sort by weight
    parent = list(range(vertices))
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        parent[find(x)] = find(y)
    
    mst_cost = 0
    for u, v, weight in edges:
        if find(u) != find(v):
            union(u, v)
            mst_cost += weight
    
    return mst_cost

# Example Usage
edges = [
    (0, 1, 4),
    (0, 2, 1),
    (1, 2, 2),
    (1, 3, 5),
    (2, 3, 8)
]
print(kruskal(edges, 4))  # Output: 7
```

---

### 8. **Topological Sort**

#### **When to Use:**
- Solve problems with dependencies in a Directed Acyclic Graph (DAG).

#### **How It Works:**
Uses DFS to order nodes.

```python
def topological_sort(graph, vertices):
    visited = set()
    stack = []
    
    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(node)
    
    for v in range(vertices):
        if v not in visited:
            dfs(v)
    
    return stack[::-1]

# Example Usage
graph = {
    0: [1, 2],
    1: [3],
    2: [3],
    3: []
}
print(topological_sort(graph, 4))  # Output: [0, 2, 1, 3]
```

---
