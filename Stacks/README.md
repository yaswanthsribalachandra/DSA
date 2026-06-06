# Stacks

This directory contains implementations of stack data structure and stack-based algorithms.

## 📚 About Stacks

Stack is a **LIFO (Last In First Out)** data structure where elements are added and removed from the same end (top).

## 📁 Files

- `stacks.py` - Core stack implementation with push/pop operations
- `queueusingstack.py` - Implement queue using two stacks

## 🎯 Core Operations

```python
# Stack operations:
push(element)    # Add element to top - O(1)
pop()            # Remove from top - O(1)
peek()           # View top element - O(1)
isEmpty()        # Check if empty - O(1)
size()           # Get stack size - O(1)
```

## ⏱️ Time Complexities

| Operation | Time |
|-----------|------|
| Push | O(1) |
| Pop | O(1) |
| Peek | O(1) |
| Search | O(n) |
| Space | O(n) |

## 💡 Common Applications

1. **Expression Evaluation** - Checking balanced parentheses, evaluating postfix/infix expressions
2. **Backtracking** - Undo/Redo functionality, maze solving, problem backtracking
3. **Function Call Stack** - Recursion, function calls, return addresses
4. **Web Browser** - Back button history
5. **Text Editor** - Undo operations
6. **Depth-First Search** - Graph/tree traversal

## 🔗 Related Concepts

- **Queues** - Opposite of stack (FIFO)
- **Linked List** - Can be used to implement stacks
- **Recursion** - Uses call stack internally
- **DFS** - Uses stack for traversal

## 📖 Prerequisites

- Arrays
- LinkedList (recommended for understanding implementation)
- Basic Python

## 🚀 Next Steps

1. Master stack operations
2. Solve balanced parentheses problem
3. Implement expression evaluation
4. Study **Queues** (FIFO counterpart)
5. Learn **Recursion** and backtracking

## 💡 Tips

- Stack is like a pile of plates - you add and remove from the top
- Use stacks for problems requiring "undo" functionality
- Compare with queues to understand LIFO vs FIFO
- Practice implementing stack using arrays and linked lists

---

**Remember**: Understanding stacks is crucial for understanding recursion and many advanced algorithms!
