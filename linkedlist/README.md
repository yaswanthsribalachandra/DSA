# Linked Lists

This directory contains implementations of linked list data structures including singly linked lists, doubly linked lists, and stack/queue implementations using linked lists.

## 📚 About Linked Lists

A linked list is a linear data structure where elements (nodes) are connected via pointers. Unlike arrays, linked lists allow efficient insertion and deletion at any position.

## 📁 Files

- `linkedlist.py` - Singly linked list implementation
- `doublelinkedlist.py` - Doubly linked list implementation
- `stacks.py` - Stack implementation using linked list
- `queues.py` - Queue implementation using linked list

## 🎯 Core Concepts

### Node Structure
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # For singly linked list
```

### Singly Linked List Operations
```
Access:    O(n)  - Must traverse from head
Search:    O(n)  - Linear search through nodes
Insert:    O(1)  - If position known
Delete:    O(1)  - If position known
```

### Doubly Linked List Operations
```
Access:    O(n)  - Faster if close to tail
Search:    O(n)  - Can search from both ends
Insert:    O(1)  - If position known
Delete:    O(1)  - If position known
```

## 📊 Comparison with Arrays

| Operation | Array | Linked List |
|-----------|-------|-------------|
| Access | O(1) | O(n) |
| Search | O(n) | O(n) |
| Insert | O(n) | O(1)* |
| Delete | O(n) | O(1)* |
| Space | O(n) | O(n) + pointers |

*If position is already known

## 🔗 Advantages & Disadvantages

### Advantages
- ✅ Efficient insertion/deletion at any position
- ✅ Dynamic size - no pre-allocation needed
- ✅ Memory used only for stored elements
- ✅ No need for contiguous memory

### Disadvantages
- ❌ No random access (must traverse)
- ❌ Extra memory for pointers
- ❌ Cache unfriendly
- ❌ Slower search than arrays

## 🎯 Linked List Types

### 1. Singly Linked List
- Each node points to next node only
- Simple, but can only traverse forward
- Most common type

### 2. Doubly Linked List
- Each node points to next and previous
- Allows bi-directional traversal
- More memory overhead

### 3. Circular Linked List
- Last node points back to first node
- No end sentinel
- Useful for round-robin scheduling

## 💡 Common Operations

### Traversal - O(n)
```python
def traverse(head):
    current = head
    while current:
        print(current.data)
        current = current.next
```

### Insertion at Beginning - O(1)
```python
def insert_at_beginning(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node
```

### Deletion - O(1) or O(n)
```python
def delete_node(head, data):
    if head.data == data:
        return head.next
    current = head
    while current.next:
        if current.next.data == data:
            current.next = current.next.next
            return head
        current = current.next
    return head
```

## 🚀 Common Problems

1. **Reverse Linked List** - O(n)
2. **Detect Cycle** - O(n)
3. **Find Middle** - O(n)
4. **Merge Sorted Lists** - O(n+m)
5. **Palindrome Check** - O(n)
6. **Intersection Point** - O(n)

## 📖 Prerequisites

- Arrays (comparison)
- Pointers/References
- Basic loops and conditionals
- Stack/Queue concepts (for implementations)

## 🎓 Learning Path

1. Understand **Node structure**
2. Master **singly linked list** operations
3. Learn **doubly linked list**
4. Implement **Stack** using linked list
5. Implement **Queue** using linked list
6. Solve common **linked list problems**

## ⚠️ Common Mistakes

- **Memory leaks** - Not freeing nodes (in C/C++)
- **Infinite loops** - Wrong traversal logic
- **Null pointer exceptions** - Not checking for None
- **Lost references** - Overwriting node pointers
- **Circular reference** - Accidental cycles

## 💡 Tips

- Draw the linked list while solving problems
- Use two-pointer technique for many problems
- Test with edge cases (empty, single node, etc.)
- Use visualization to debug
- Compare with array operations to understand trade-offs

## 🔍 Debugging Techniques

- Print node values at each step
- Visualize pointer connections
- Use assertions to verify state
- Test on small inputs first
- Draw diagrams before coding

---

**Remember**: Linked lists are essential for understanding more complex data structures! 🔗
