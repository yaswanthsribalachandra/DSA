# Binary Trees

This directory contains implementations of binary tree data structures and tree traversal algorithms.

## 📚 About Binary Trees

A binary tree is a hierarchical data structure where each node has at most two children (left and right). Trees are fundamental for many algorithms and data structures.

## 📁 Files

- `DFS.py` - Depth-First Search traversals (Inorder, Preorder, Postorder)
- `BFS.py` - Breadth-First Search (Level-order traversal)

## 🎯 Core Concepts

### Tree Terminology
- **Root**: Top node of the tree
- **Leaf**: Node with no children
- **Height**: Longest path from node to leaf
- **Depth**: Distance from root to node
- **Parent/Child**: Hierarchical relationships

### Node Structure
```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
```

## 📊 Tree Traversal Methods

### 1. Depth-First Search (DFS) - O(n)

#### Inorder (Left, Root, Right)
```
Used for: BST to get sorted order
Example: 4 2 5 1 3 (for BST example)
```

#### Preorder (Root, Left, Right)
```
Used for: Create copy, serialize tree
Example: 1 2 4 5 3
```

#### Postorder (Left, Right, Root)
```
Used for: Delete tree, expression evaluation
Example: 4 5 2 3 1
```

### 2. Breadth-First Search (BFS) - O(n)

#### Level-order Traversal
```
Used for: Level-by-level processing
Example: 1 2 3 4 5
Space: O(w) where w is max width
```

## 💡 Tips

- Draw the tree before solving problems
- Use recursion for most tree problems
- Test with edge cases (empty, single node)
- Visualize the tree at each step

---

**Remember**: Trees are everywhere in computer science! Master them well! 🌳
