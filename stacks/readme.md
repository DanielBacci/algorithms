### **Stacks**

A **stack** is a linear data structure that follows the **Last In, First Out (LIFO)** principle. The last item added to the stack is the first one removed. Stacks are widely used in programming for tasks like function calls, recursion, and evaluating expressions.

---

### **Memory Structure of Stacks**

1. **Dynamic Nature**:
   - A stack can be implemented using an **array** (fixed size) or a **linked list** (dynamic size).
   - Arrays require contiguous memory, while linked lists use non-contiguous memory with pointers.

2. **Growth and Shrinkage**:
   - **Array-based Stack**: Has a fixed size unless dynamically resized (e.g., in Python lists or Java's `ArrayList`).
   - **Linked List-based Stack**: Grows and shrinks dynamically, but uses more memory per element due to pointers.

---

### **Operations and Big O Complexity**

| **Operation**       | **Description**                                     | **Time Complexity** |
|----------------------|-----------------------------------------------------|----------------------|
| `push(element)`      | Adds an element to the top of the stack.            | \( O(1) \)           |
| `pop()`              | Removes the top element from the stack.             | \( O(1) \)           |
| `peek()` or `top()`  | Returns the top element without removing it.         | \( O(1) \)           |
| `isEmpty()`          | Checks if the stack is empty.                       | \( O(1) \)           |
| `size()`             | Returns the number of elements in the stack.        | \( O(1) \)           |

---

### **Memory Usage**

#### Array-Based Stack:
- **Memory Overhead**: Minimal; only data is stored.
- **Resizing Cost**: If resizing is required, a new array is allocated, and elements are copied, which is \( O(n) \) for resizing.

#### Linked List-Based Stack:
- **Memory Overhead**: Each element requires additional memory for a pointer to the next node.
- **Dynamic Size**: Memory usage adjusts dynamically based on the number of elements.

---

### **Key Features**

1. **LIFO Behavior**:
   - The most recently added element is accessed first.
   - No direct access to elements in the middle of the stack.

2. **Efficient for Certain Tasks**:
   - Tracks function calls (call stack in programming).
   - Used for undo functionality in editors.
   - Evaluates expressions (e.g., converting infix to postfix).

---

### **Common Use Cases**

1. **Function Call Stack**:
   - The system uses a stack to manage function calls and local variables during execution.
   - Example: Recursive functions push and pop calls onto the stack.

2. **Expression Evaluation**:
   - Used for parsing and evaluating mathematical expressions (e.g., converting infix to postfix or evaluating postfix expressions).

3. **Backtracking**:
   - Helps in algorithms like DFS (Depth First Search), solving mazes, and undo operations.

4. **Balancing Symbols**:
   - Used to check for balanced parentheses, braces, or brackets in strings.

5. **Browser History or Undo Features**:
   - Tracks actions in applications to enable undo or navigation back.

---

### **Comparison with Other Data Structures**

| **Aspect**           | **Array-Based Stack**         | **Linked List-Based Stack**         |
|-----------------------|-------------------------------|--------------------------------------|
| **Memory Usage**      | Lower (no extra pointers)     | Higher (due to pointers)            |
| **Resizing**          | Requires reallocation         | Dynamic resizing without overhead   |
| **Performance**       | \( O(1) \) for all operations | \( O(1) \) for all operations       |

---

### **When to Use Stacks**

- When you need **LIFO** access to data.
- For tasks that involve recursion, expression evaluation, or balanced symbols.
- If memory overhead isn’t a concern, linked list-based stacks offer dynamic resizing.
- If fixed memory and faster access are priorities, array-based stacks are ideal.

---
