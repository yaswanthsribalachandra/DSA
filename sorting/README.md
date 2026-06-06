# Sorting Algorithms

This directory contains implementations of various sorting algorithms with different time and space complexity characteristics.

## 📚 Sorting Algorithms Overview

Sorting is one of the most fundamental algorithms in computer science. Different algorithms have different trade-offs in time complexity, space complexity, stability, and use cases.

## 📁 Files

- `bubblesort.py` - Bubble Sort - **O(n²)** - Simple, stable
- `selection.py` - Selection Sort - **O(n²)** - In-place, unstable
- `insertion.py` - Insertion Sort - **O(n²)** - Stable, good for nearly sorted
- `merge.py` - Merge Sort - **O(n log n)** - Stable, requires O(n) extra space
- `quicksort.py` - Quick Sort - **O(n log n)** average - In-place, unstable
- `hash.py` - Counting/Hash Sort - **O(n+k)** - For integer ranges

## 📊 Comparison Table

| Algorithm | Best | Average | Worst | Space | Stable | In-Place |
|-----------|------|---------|-------|-------|--------|----------|
| Bubble | O(n) | O(n²) | O(n²) | O(1) | ✅ | ✅ |
| Selection | O(n²) | O(n²) | O(n²) | O(1) | ❌ | ✅ |
| Insertion | O(n) | O(n²) | O(n²) | O(1) | ✅ | ✅ |
| Merge | O(n log n) | O(n log n) | O(n log n) | O(n) | ✅ | ❌ |
| Quick | O(n log n) | O(n log n) | O(n²) | O(log n) | ❌ | ✅ |
| Counting | O(n+k) | O(n+k) | O(n+k) | O(k) | ✅ | ❌ |

## 🎯 Algorithm Details

### 1. Bubble Sort
- Repeatedly compares adjacent elements
- Best for: Learning, small datasets, nearly sorted data
- Time: **O(n²)**, Space: **O(1)**

### 2. Selection Sort
- Finds minimum and places at beginning
- Best for: Minimizing memory writes
- Time: **O(n²)**, Space: **O(1)**

### 3. Insertion Sort
- Builds sorted array incrementally
- Best for: Small arrays, nearly sorted data
- Time: **O(n)** best, **O(n²)** worst, Space: **O(1)**

### 4. Merge Sort
- Divide and conquer approach
- Best for: Consistent performance, stability needed
- Time: **O(n log n)**, Space: **O(n)**

### 5. Quick Sort
- Partition-based approach
- Best for: General purpose, average performance
- Time: **O(n log n)** average, **O(n²)** worst, Space: **O(log n)**

### 6. Counting Sort
- Uses counting array for integers
- Best for: Integer ranges, linear time requirement
- Time: **O(n+k)**, Space: **O(k)**

## 💡 Choosing the Right Algorithm

### Use Bubble Sort when:
- Learning sorting concepts
- Dataset is very small (< 10 elements)
- Already nearly sorted
- Memory is not a concern

### Use Insertion Sort when:
- Small dataset (< 50 elements)
- Data is nearly sorted
- Online sorting needed (sorts while receiving data)
- Stable sorting required

### Use Merge Sort when:
- Stability is important
- Consistent O(n log n) performance needed
- External sorting (data doesn't fit in memory)
- Parallel sorting

### Use Quick Sort when:
- General purpose sorting
- In-place sorting needed
- Average case O(n log n) is acceptable
- Cache-friendly is important

### Use Counting Sort when:
- Sorting integers in small range
- Linear time is critical
- Stability needed
- Space available for counting array

## 🔗 Related Algorithms

- **Heap Sort** - Uses heap data structure
- **Radix Sort** - Extends counting sort for larger ranges
- **Bucket Sort** - Distributes elements into buckets
- **Tim Sort** - Hybrid merge + insertion sort (used in Python)

## 📖 Prerequisites

- Arrays
- Basic loops and conditionals
- Time complexity analysis
- Recursion (for divide and conquer sorts)

## 🚀 Learning Path

1. Start with **Bubble Sort** - Understand basic swapping
2. Learn **Selection Sort** - Minimum finding
3. Study **Insertion Sort** - Incremental building
4. Master **Merge Sort** - Divide and conquer
5. Practice **Quick Sort** - Partitioning
6. Explore **Counting Sort** - Linear sorting

## 💡 Tips

- Visualize the algorithm before coding
- Understand the logic, don't memorize code
- Compare different sorting algorithms
- Analyze time and space complexity
- Practice implementing from memory
- Test edge cases (empty, single, duplicates)

## 🧪 Test Cases

Every sorting algorithm should handle:
- ✅ Empty array
- ✅ Single element
- ✅ Already sorted array
- ✅ Reverse sorted array
- ✅ Array with duplicates
- ✅ Random array
- ✅ Large arrays

---

**Remember**: Different sorting algorithms for different situations!
