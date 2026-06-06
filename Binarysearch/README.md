# Binary Search

This directory contains binary search implementations and related algorithms.

## 📚 About Binary Search

Binary Search is an efficient algorithm for searching in **sorted arrays** with O(log n) time complexity.

## 📊 How It Works

```
Search for 7 in [1, 3, 5, 7, 9, 11]

Step 1: mid = 5, not found
        [1, 3, 5] | [7, 9, 11]
        
Step 2: mid = 8, not found (9)
        [7] | [9, 11]
        
Step 3: mid = 7, FOUND!
```

## ⏱️ Complexity

| Complexity | Value |
|-----------|-------|
| Time | O(log n) |
| Space | O(1) recursive: O(log n) |

## ✅ Requirements

- Array must be **sorted**
- Works with any comparable elements

## 💡 Variants

- Lower bound search
- Upper bound search
- First occurrence
- Last occurrence
- Search in rotated array

---

**Binary Search is essential for optimization problems!** 🔍
