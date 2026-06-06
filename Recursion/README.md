# Recursion

This directory contains implementations demonstrating recursive programming concepts and patterns.

## 📚 About Recursion

Recursion is a programming technique where a function calls itself to solve a problem by breaking it into smaller sub-problems.

## 🎯 Core Concepts

Every recursive function must have:
1. **Base Case** - Condition to stop recursion and return a value
2. **Recursive Case** - Function calls itself with modified parameters
3. **Progress** - Each recursive call must move closer to base case

## 📁 Files

- `basics.py` - Recursive fundamentals and simple patterns
- `print_name.py` - Print name N times recursively
- `print_nums.py` - Print numbers 1 to N recursively
- `print_rev_nums.py` - Print numbers N to 1 (reverse)
- `print_backtrack_rev.py` - Backtracking to print numbers
- `print_nums_backtracking.py` - Backtracking number printing
- `sum_parameter.py` - Calculate sum using parameter passing
- `sum_functional.py` - Calculate sum using return values

## 📊 Types of Recursion

### 1. **Linear Recursion** - O(n)
```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)
```

### 2. **Tree Recursion** - O(2^n)
```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

### 3. **Backtracking** - Explore all solutions
```python
def permutations(arr, l, r):
    if l == r:
        print(arr)
    else:
        for i in range(l, r):
            # Swap
            arr[l], arr[i] = arr[i], arr[l]
            # Recurse
            permutations(arr, l+1, r)
            # Backtrack
            arr[l], arr[i] = arr[i], arr[l]
```

## ⏱️ Common Time Complexities

| Pattern | Complexity | Example |
|---------|-----------|---------|
| Single recursive call | O(n) | Factorial, linear search |
| Two recursive calls | O(2^n) | Naive Fibonacci |
| Divide and conquer | O(n log n) | Merge Sort, Binary Search |

## 🔗 Call Stack Visualization

```
factorial(5)
  └─ factorial(4)
      └─ factorial(3)
          └─ factorial(2)
              └─ factorial(1)  [BASE CASE - returns 1]
              returns 1 * 2 = 2
          returns 2 * 3 = 6
      returns 6 * 4 = 24
  returns 24 * 5 = 120
```

## 💡 When to Use Recursion

✅ **Good for:**
- Tree traversals
- Backtracking problems
- Divide and conquer
- Mathematical calculations
- DFS in graphs

❌ **Avoid when:**
- Simple loops are sufficient
- Deep recursion (stack overflow)
- Performance-critical code
- No clear base case

## 🚀 Optimization Techniques

### 1. **Memoization** - Cache results
```python
def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]
```

### 2. **Tail Recursion** - Last call optimization
```python
def factorial_tail(n, acc=1):
    if n <= 1:
        return acc
    return factorial_tail(n-1, n*acc)
```

## 📖 Prerequisites

- Arrays
- Basic loops and conditionals
- Understanding function calls
- Time complexity analysis

## 🎯 Learning Path

1. Start with **print_name.py** - Simple recursion
2. Practice **factorial** and **fibonacci**
3. Learn **backtracking** patterns
4. Apply to **tree traversals**
5. Master **divide and conquer** (Merge Sort, Quick Sort)
6. Explore **dynamic programming** (memoization)

## ⚠️ Common Mistakes

- **Missing base case** - Infinite recursion
- **Wrong base case** - Incorrect output
- **Modifying global state** - Hard to debug
- **Deep recursion** - Stack overflow
- **Inefficient recursion** - Redundant calculations

## 💡 Tips

- Draw the recursion tree to understand flow
- Always identify base case first
- Test with small inputs
- Use memoization for repeated calculations
- Compare recursion with iteration

---

**Remember**: "To understand recursion, you must first understand recursion!" 🔄
