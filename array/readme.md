## **Array**  
Arrays are collections of elements of the same type, stored in contiguous memory locations.

### **Types of Arrays**
#### **One-dimensional (1D)**  
A linear array:  
```
[1, 2, 3, 4]
```

#### **Multidimensional**  
Matrices or tables with multiple rows and columns:  
```
[
 [1, 2, 3, 4],
 [5, 6, 7, 8]
]
```

---

### **Key Features**
- **Fixed Size**: The length of the array is defined at creation and cannot be changed.  
- **Index-based Access**: Each element can be accessed directly via its index.

---

### **Time Complexity - Big O**
| Operation                  | Complexity | Notes                                                     |
|----------------------------|------------|----------------------------------------------------------|
| **Access by index**         | \(O(1)\)    | Direct access without depending on the array's size.      |
| **Search (value)**          | \(O(n)\)    | In the worst case, the entire array must be traversed.    |
| **Insert at the end**       | \(O(1)\)    | Simply appends the element (in dynamic arrays).           |
| **Insert at any position**  | \(O(n)\)    | Elements must be shifted to make room.                   |
| **Remove from the end**     | \(O(1)\)    | Directly removes the last element.                       |
| **Remove from any position**| \(O(n)\)    | Elements must be shifted after the removal.              |

---

### **Common Use Cases**
1. **Sorting and Searching Algorithms**:
   - Arrays are often used as input for algorithms like Binary Search, Quick Sort, Merge Sort, etc.
2. **Derived Data Structures**:
   - Stacks, Queues, and Heaps can be implemented using arrays.
3. **Data Representation**:
   - Graphs, adjacency matrices, and tables.

---

### **Advantages**
- **Fast Access**: Accessing an element by index is instantaneous (\(O(1)\)).
- **Memory Efficiency**: Compact representation, especially compared to linked lists.

### **Disadvantages**
- **Fixed Size**: Cannot grow or shrink after creation (unless using dynamic arrays).  
- **Costly Modifications**: Inserting or deleting elements in the middle requires shifting, making it inefficient for frequent modifications.

---
