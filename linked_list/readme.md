## **Linked List**  
A linked list is a linear data structure consisting of nodes, where each node contains a value and a reference (or pointer) to the next node.  

---

### **Types of Linked Lists**
#### **Singly Linked List**  
Each node points to the next node:  
```
[1] -> [2] -> [3] -> [4] -> None
```

#### **Doubly Linked List**  
Each node points to both the previous and the next node:  
```
None <- [1] <-> [2] <-> [3] <-> [4] -> None
```

#### **Circular Linked List**  
The last node points back to the first node (can be singly or doubly linked):  
```
[1] -> [2] -> [3] -> [4] -+
 ^-----------------------+
```

---

### **Key Features**
- **Dynamic Size**: Unlike arrays, linked lists can grow or shrink as needed.  
- **Sequential Access**: Traversal must happen node by node.  
- **Efficient Insertions/Deletions**: No need for element shifting; pointers are adjusted.  

---

### **Time Complexity - Big O**
| Operation                     | Complexity | Notes                                                     |
|--------------------------------|------------|----------------------------------------------------------|
| **Access by index**            | \(O(n)\)    | Requires traversing the list from the head.              |
| **Search (value)**             | \(O(n)\)    | Must traverse the entire list in the worst case.         |
| **Insert at the head**         | \(O(1)\)    | Adjust the pointer of the new node to the current head.  |
| **Insert at the tail**         | \(O(n)\)    | Traverse to the last node unless a tail pointer is kept. |
| **Insert at a specific position** | \(O(n)\) | Must traverse to the desired position.                   |
| **Delete at the head**         | \(O(1)\)    | Adjust the head pointer.                                 |
| **Delete at the tail**         | \(O(n)\)    | Traverse to the second-to-last node.                    |
| **Delete a specific position** | \(O(n)\)    | Must traverse to find the node.                         |

---

### **Practical Limitations**
- **Memory Overhead**: Each node stores both data and pointers, consuming more memory than arrays.  
- **Sequential Access**: Slower access compared to arrays since direct indexing isn't possible.

---

### **Common Use Cases**
1. **Dynamic Data Structures**:
   - Implement stacks, queues, or deques.
2. **Efficient Insertions/Deletions**:
   - Useful for scenarios where frequent insertions or deletions are required, e.g., undo functionality.
3. **Graph Representation**:
   - Adjacency lists in graph algorithms.

---

### **Advantages**
- **Dynamic Size**: No need to declare size in advance.  
- **Efficient Insertions/Deletions**: Especially at the head or tail.  

### **Disadvantages**
- **Memory Overhead**: Extra memory is needed for pointers.  
- **Sequential Access**: Access is slower compared to arrays.  

---
