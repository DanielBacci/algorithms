### **Graphs**

Graphs are one of the most versatile and widely used data structures. They represent relationships between objects, making them essential for problems involving connectivity, networks, paths, and hierarchies. Here’s a detailed overview:

---

### **Features**
- **Vertices (Nodes):** Represent entities.
- **Edges:** Represent relationships or connections between vertices.
  - **Directed Edge:** Has a direction (e.g., A → B).
  - **Undirected Edge:** No direction (e.g., A ↔ B).
- **Weight:** Represents the cost or value of traversing an edge (used in weighted graphs).

---

### **Types of Graphs**

| **Type**             | **Description**                                                                                   | **Example Use Cases**                                   |
|-----------------------|---------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| **Directed Graph**     | Edges have a direction (e.g., A → B).                                                           | Traffic flow, dependencies (e.g., task scheduling).    |
| **Undirected Graph**   | Edges have no direction (e.g., A ↔ B).                                                          | Social networks, road maps.                           |
| **Weighted Graph**     | Edges have weights (e.g., distance, cost).                                                     | Shortest path algorithms (e.g., Dijkstra’s).          |
| **Unweighted Graph**   | Edges have no weights.                                                                          | Connectivity problems.                                |
| **Cyclic Graph**       | Contains at least one cycle (a path that starts and ends at the same vertex).                   | Feedback loops.                                       |
| **Acyclic Graph**      | Contains no cycles.                                                                             | DAGs (e.g., task scheduling, data pipelines).         |
| **Connected Graph**    | Every vertex is reachable from any other vertex (for undirected graphs).                        | Network design.                                       |
| **Disconnected Graph** | Contains one or more isolated components (subgraphs).                                          | Clustering or grouping problems.                     |
| **Sparse Graph**       | Few edges relative to the number of vertices (\( |E| \approx |V| \)).                          | Large but lightly connected networks.                |
| **Dense Graph**        | Many edges relative to the number of vertices (\( |E| \approx |V|^2 \)).                       | Fully connected networks.                            |

---

### **Graph Representations**

1. **Adjacency Matrix**
   - A 2D array where \( matrix[i][j] = 1 \) (or the weight) if there is an edge from vertex \( i \) to \( j \), otherwise 0.
   - **Pros:** Fast lookup for edge existence (\( O(1) \)).
   - **Cons:** High space complexity (\( O(V^2) \)).
   - **Use Case:** Dense graphs.

2. **Adjacency List**
   - A list of lists where each vertex points to a list of adjacent vertices (or edges with weights).
   - **Pros:** Space-efficient for sparse graphs (\( O(V + E) \)).
   - **Cons:** Slower lookup for edge existence.
   - **Use Case:** Sparse graphs.

3. **Edge List**
   - A list of edges, where each edge is represented as a pair (or triplet for weighted graphs).
   - **Pros:** Simple representation.
   - **Cons:** Inefficient for lookups.
   - **Use Case:** Situations where edges are frequently added or removed.

---

### **Common Operations and Their Complexities**

| **Operation**                | **Adjacency Matrix** | **Adjacency List** |
|-------------------------------|----------------------|--------------------|
| Check if edge exists          | \( O(1) \)          | \( O(V) \)         |
| Add edge                      | \( O(1) \)          | \( O(1) \)         |
| Remove edge                   | \( O(1) \)          | \( O(V) \)         |
| Find neighbors of a vertex    | \( O(V) \)          | \( O(\text{degree}) \) |
| Space Complexity              | \( O(V^2) \)        | \( O(V + E) \)     |

---

### **Graph Traversals**

1. **Breadth-First Search (BFS):**
   - Traverses the graph layer by layer (uses a queue).
   - **Time Complexity:** \( O(V + E) \) (Adjacency List).
   - **Applications:** Shortest path in unweighted graphs, finding connected components.

2. **Depth-First Search (DFS):**
   - Explores as far as possible along one branch before backtracking (uses a stack or recursion).
   - **Time Complexity:** \( O(V + E) \) (Adjacency List).
   - **Applications:** Detecting cycles, topological sorting, solving mazes.

3. **Dijkstra’s Algorithm:**
   - Finds the shortest path in weighted graphs (non-negative weights).
   - **Time Complexity:** \( O((V + E) \log V) \) (using a priority queue).

4. **Bellman-Ford Algorithm:**
   - Finds the shortest path in graphs with negative weights.
   - **Time Complexity:** \( O(VE) \).

5. **Floyd-Warshall Algorithm:**
   - Finds shortest paths between all pairs of vertices.
   - **Time Complexity:** \( O(V^3) \).

6. **Kruskal’s Algorithm:**
   - Finds the Minimum Spanning Tree (MST) using edge weights.
   - **Time Complexity:** \( O(E \log E) \).

7. **Prim’s Algorithm:**
   - Finds the MST, focusing on connected components.
   - **Time Complexity:** \( O((V + E) \log V) \).

8. **Topological Sort:**
   - Linear ordering of vertices in a Directed Acyclic Graph (DAG).
   - **Time Complexity:** \( O(V + E) \).

---

### **Applications**

1. **Real-World Problems:**
   - **Social Networks:** Find mutual friends, suggest connections.
   - **Navigation Systems:** Shortest paths, traffic optimization.
   - **Web Crawling:** Page ranking, finding cycles.
   - **Supply Chains:** Optimizing routes and dependencies.

2. **Algorithmic Problems:**
   - Finding connected components.
   - Detecting cycles or strongly connected components.
   - Solving scheduling problems using DAGs.

---

### **Big O Summary**

| **Operation**          | **Adjacency List**       | **Adjacency Matrix**     |
|-------------------------|--------------------------|--------------------------|
| Space Complexity        | \( O(V + E) \)          | \( O(V^2) \)             |
| Add Edge                | \( O(1) \)              | \( O(1) \)               |
| Remove Edge             | \( O(V) \)              | \( O(1) \)               |
| BFS/DFS                 | \( O(V + E) \)          | \( O(V^2) \)             |
| Dijkstra’s Algorithm    | \( O((V + E) \log V) \) | \( O(V^2) \)             |

---

