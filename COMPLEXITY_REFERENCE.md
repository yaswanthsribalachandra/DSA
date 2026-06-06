# Complexity Reference - Big O Cheat Sheet

Quick reference for time and space complexity of common algorithms and data structures.

## 📊 Sorting Algorithms Comparison

| Algorithm | Best | Average | Worst | Space | Stable | Notes |
|-----------|------|---------|-------|-------|--------|-------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes | Simple, good for nearly sorted |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | No | Minimizes writes |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes | Good for small/nearly sorted |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes | Consistent, stable |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | No | Fast average, good pivot important |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | No | Consistent |
| Count Sort | O(n+k) | O(n+k) | O(n+k) | O(k) | Yes | For range of integers |
| Radix Sort | O(nk) | O(nk) | O(nk) | O(n+k) | Yes | For integer keys |

**Legend**: n = number of elements, k = range of input

---

## 🔍 Searching Algorithms

| Algorithm | Best | Average | Worst | Space | Notes |
|-----------|------|---------|-------|-------|-------|
| Linear Search | O(1) | O(n) | O(n) | O(1) | Works on unsorted arrays |
| Binary Search | O(1) | O(log n) | O(log n) | O(1) | Requires sorted array |
| Binary Search Tree | O(log n) | O(log n) | O(n) | O(n) | Unbalanced tree is worst |

---

## 📈 Data Structure Operations

### Array/List
```
Access:    O(1)  - Direct index access
Search:    O(n)  - Need to check elements
Insert:    O(n)  - May require shift
Delete:    O(n)  - May require shift
Space:     O(n)
```

### Linked List
```
Access:    O(n)  - Must traverse from head
Search:    O(n)  - Must traverse elements
Insert:    O(1)  - If position known
Delete:    O(1)  - If position known
Space:     O(n)
```

### Doubly Linked List
```
Access:    O(n)  - Can start from head or tail
Search:    O(n)  - Must traverse
Insert:    O(1)  - If position known
Delete:    O(1)  - If position known
Space:     O(n)
```

### Stack (using array)
```
Push:      O(1)  - Amortized if dynamic
Pop:       O(1)
Peek:      O(1)
Search:    O(n)
Space:     O(n)
```

### Queue (using array)
```
Enqueue:   O(1)  - Amortized if dynamic
Dequeue:   O(1)
Peek:      O(1)
Search:    O(n)
Space:     O(n)
```

### Binary Search Tree
```
Access:    O(log n) - Average
Search:    O(log n) - Average, O(n) worst
Insert:    O(log n) - Average
Delete:    O(log n) - Average
Space:     O(n)
Best for:  Ordered data, range queries
Worst:     Skewed tree (unbalanced)
```

### Hash Table
```
Insert:    O(1)  - Average
Delete:    O(1)  - Average
Search:    O(1)  - Average, O(n) worst
Space:     O(n)
Worst:     High collision rate
Note:      Expected O(1), not guaranteed
```

### Binary Heap (Min/Max)
```
Insert:    O(log n)
Delete Min: O(log n)
Get Min:   O(1)
Heapify:   O(n)
Space:     O(n)
```

### Graph Representations
```
Adjacency Matrix:
  Space:    O(V²)
  Add Edge: O(1)
  Query:    O(1)

Adjacency List:
  Space:    O(V + E)
  Add Edge: O(1)
  Query:    O(degree)
```

---

## 🌳 Tree Operations

### Binary Tree Traversals
```
Inorder:      O(n) time, O(h) space
Preorder:     O(n) time, O(h) space
Postorder:    O(n) time, O(h) space
Level Order:  O(n) time, O(w) space
```
**h** = height of tree, **w** = max width

### Common Tree Operations
```
Search:    O(n) - Unbalanced BST
           O(log n) - Balanced BST
Insert:    O(log n) - Average
Delete:    O(log n) - Average
Find Min:  O(log n) - BST
Find Max:  O(log n) - BST
```

---

## 🔗 Recursion

### Time Complexity Analysis
- **Fibonacci (naive)**: O(2ⁿ) - exponential
- **Factorial**: O(n) - linear
- **Binary Search (recursive)**: O(log n)
- **Merge Sort**: O(n log n)
- **Quick Sort**: O(n log n) average, O(n²) worst

### Space Complexity
- **Call Stack**: O(h) where h = recursion depth
- **Additional Space**: Problem dependent

---

## 🧩 Common Patterns

### Divide and Conquer
```
Complexity: O(n log n) typically
Examples: Merge Sort, Quick Sort, Binary Search
Pattern: Divide problem → Solve sub-problems → Combine
```

### Dynamic Programming
```
Without Optimization: O(2ⁿ) exponential
With Memoization: O(n) to O(n²) depending on problem
Space: O(n) for DP table + O(n) for recursion
```

### Greedy Algorithms
```
Complexity: Varies
Space: Often O(1) or O(n)
Note: Fast but doesn't always give optimal solution
```

### Backtracking
```
Worst Case: O(N^N) where N is problem size
Examples: Permutations, combinations, Sudoku
Space: O(N) for recursion depth
```

---

## 📊 Space Complexity Breakdown

### Common Space Complexities
```
O(1)        - Constant space (variables, pointers)
O(log n)    - Recursion depth (binary search)
O(n)        - Linear space (arrays, lists)
O(n log n)  - Merge sort (n for output, log n for recursion)
O(n²)       - 2D arrays, some DP solutions
O(2ⁿ)       - Combinations, subsets
O(n!)       - Permutations
```

### Space Optimization
```
In-place algorithms:   O(1) additional space
Additional arrays:     O(n) additional space
Recursion stack:       O(h) for height
```

---

## 🎯 Quick Decision Guide

### Choosing Sorting Algorithm
- **Need stable sort?** → Merge Sort, Bubble Sort, Insertion Sort
- **Limited memory?** → Quick Sort, Heap Sort (O(log n) space)
- **Nearly sorted data?** → Insertion Sort
- **Small dataset?** → Insertion Sort, Bubble Sort
- **Large random data?** → Quick Sort, Merge Sort
- **Integer data with small range?** → Counting Sort, Radix Sort

### Choosing Data Structure
- **Need ordered traversal?** → Sorted Array, BST
- **Need fast search?** → Hash Table
- **Need LIFO?** → Stack
- **Need FIFO?** → Queue
- **Need dynamic sizing?** → Linked List, Dynamic Array
- **Need range queries?** → Binary Search Tree, Segment Tree

---

## 📝 Master Equation (Recurrence Relations)

### Master Theorem
For recurrence: T(n) = a·T(n/b) + f(n)

**Case 1**: f(n) = O(n^(log_b(a) - ε)) → T(n) = O(n^(log_b(a)))
**Case 2**: f(n) = O(n^(log_b(a)) · log^k(n)) → T(n) = O(n^(log_b(a)) · log^(k+1)(n))
**Case 3**: f(n) = O(n^(log_b(a) + ε)) → T(n) = O(f(n))

**Examples**:
- Merge Sort: T(n) = 2·T(n/2) + O(n) → O(n log n)
- Binary Search: T(n) = T(n/2) + O(1) → O(log n)
- Quick Sort avg: T(n) = 2·T(n/2) + O(n) → O(n log n)

---

## 💡 Tips for Complexity Analysis

1. **Identify the operations**: Count loops, recursive calls
2. **Find the pattern**: Look for n, n², log n, 2ⁿ
3. **Ignore constants**: O(2n) = O(n), O(n+100) = O(n)
4. **Drop lower order terms**: O(n² + n) = O(n²)
5. **Consider best/average/worst**: Different inputs affect complexity
6. **Space vs Time**: Sometimes one can be traded for the other

---

**Practice analyzing complexity for every algorithm you learn!** 📚
