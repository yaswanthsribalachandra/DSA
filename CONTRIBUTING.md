# Contributing to DSA Repository

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to the DSA repository.

## 📋 Code of Conduct

Be respectful, inclusive, and professional in all interactions.

## 🔄 How to Contribute

### 1. Report Issues
- Check existing issues to avoid duplicates
- Provide clear descriptions
- Include example code when relevant
- Specify Python version and OS

### 2. Add New Algorithms/Data Structures

#### Code Quality Standards
- **Type Hints**: All functions must have type hints
  ```python
  def merge_sort(arr: List[int]) -> List[int]:
  ```
- **Docstrings**: Include comprehensive docstrings:
  ```python
  def merge_sort(arr: List[int]) -> List[int]:
      """
      Sort an array using Merge Sort algorithm.
      
      Args:
          arr: List of integers to be sorted
          
      Returns:
          Sorted list of integers
          
      Time Complexity: O(n log n) in all cases
      Space Complexity: O(n)
      
      Example:
          >>> merge_sort([5, 2, 8, 1, 9])
          [1, 2, 5, 8, 9]
      """
  ```

- **Complexity Documentation**: Always document time and space complexity
- **Error Handling**: Include input validation
  ```python
  if not arr or not isinstance(arr, list):
      raise ValueError("Input must be a non-empty list")
  ```

### 3. File Naming Conventions

- **Python files**: Use `snake_case.py`
  - ✅ `merge_sort.py`, `binary_search.py`
  - ❌ `MergeSort.py`, `mergeSort.py`

- **Folders**: Use `PascalCase` (CamelCase)
  - ✅ `Arrays`, `LinkedList`, `BinaryTrees`
  - ❌ `arrays`, `linked_list`, `binarytrees`

- **Documentation**: Use `UPPERCASE.md`
  - ✅ `README.md`, `CHANGELOG.md`
  - ❌ `readme.md`, `changelog.md`

### 4. Code Structure Example

```python
"""Module for sorting algorithms."""
from typing import List, Tuple


def bubble_sort(arr: List[int]) -> List[int]:
    """
    Sort an array using Bubble Sort algorithm.
    
    Args:
        arr: List of integers to be sorted
        
    Returns:
        Sorted list of integers
        
    Raises:
        ValueError: If arr is not a list or is empty
        
    Time Complexity: O(n²) average and worst case, O(n) best case
    Space Complexity: O(1)
    
    Example:
        >>> bubble_sort([5, 2, 8, 1, 9])
        [1, 2, 5, 8, 9]
    """
    if not arr or not isinstance(arr, list):
        raise ValueError("Input must be a non-empty list")
    
    arr = arr.copy()  # Don't modify original array
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr


# Example usage and testing
if __name__ == "__main__":
    test_arr = [5, 2, 8, 1, 9, 3, 7, 4, 6]
    result = bubble_sort(test_arr)
    print(f"Sorted array: {result}")
```

### 5. Creating Tests

Create tests in the `tests/` directory:

```python
# tests/test_sorting.py
import unittest
from sorting.bubble_sort import bubble_sort


class TestBubbleSort(unittest.TestCase):
    def test_basic_sort(self):
        self.assertEqual(bubble_sort([5, 2, 8, 1]), [1, 2, 5, 8])
    
    def test_already_sorted(self):
        self.assertEqual(bubble_sort([1, 2, 3, 4]), [1, 2, 3, 4])
    
    def test_reverse_sorted(self):
        self.assertEqual(bubble_sort([4, 3, 2, 1]), [1, 2, 3, 4])
    
    def test_single_element(self):
        self.assertEqual(bubble_sort([1]), [1])
    
    def test_empty_raises_error(self):
        with self.assertRaises(ValueError):
            bubble_sort([])


if __name__ == '__main__':
    unittest.main()
```

### 6. Documentation Requirements

When adding new algorithms:
1. Add docstring to the main function
2. Include time and space complexity
3. Add example usage in docstring
4. Create a test file
5. Update relevant `README.md` with link to new algorithm

### 7. Pull Request Process

1. Fork the repository
2. Create a feature branch: `git checkout -b add-new-algorithm`
3. Make your changes following the guidelines above
4. Run tests: `python -m pytest tests/`
5. Commit with clear messages: `git commit -m "Add merge sort algorithm"`
6. Push to your fork
7. Submit a Pull Request with:
   - Clear description of changes
   - Reference to related issues
   - List of tests added/modified

### 8. Commit Message Guidelines

- Use imperative mood: "Add algorithm" not "Added algorithm"
- Start with a capital letter
- Do not end with a period
- Reference issues when applicable: "Fix #123"

Examples:
- ✅ `Add binary search implementation`
- ✅ `Improve time complexity of quicksort`
- ✅ `Fix issue with linked list deletion (Fixes #45)`
- ❌ `fixed bugs`
- ❌ `Updated stuff`

### 9. Areas to Contribute

We welcome contributions in:
- New sorting/searching algorithms
- Optimization of existing algorithms
- Better documentation and examples
- Bug fixes
- Test coverage improvements
- Performance improvements with benchmarks
- Visualization helpers
- Problem-solving examples

### 10. Review Process

All PRs will be reviewed for:
- ✅ Code quality and style compliance
- ✅ Documentation completeness
- ✅ Test coverage
- ✅ Complexity analysis correctness
- ✅ No breaking changes
- ✅ Performance considerations

## ❓ Questions or Need Help?

- Open an issue for questions
- Check existing issues and documentation
- Participate in discussions

---

Thank you for contributing to make DSA learning better for everyone! 🎉
