# Unit Tests

This directory contains unit tests for all DSA implementations.

## 📚 Testing Structure

```
tests/
├── test_arrays.py
├── test_sorting.py
├── test_searching.py
├── test_recursion.py
└── ...
```

## 🎯 Running Tests

```bash
# Run all tests
python -m pytest tests/

# Run specific test file
python -m pytest tests/test_sorting.py

# Run with coverage
python -m pytest --cov=. tests/
```

## ✅ Test Requirements

Each algorithm should have tests for:
- ✅ Basic functionality
- ✅ Edge cases (empty, single element)
- ✅ Normal cases (typical input)
- ✅ Boundary conditions
- ✅ Error handling

## 📝 Example Test File

```python
import unittest
from Arrays.largest import largest

class TestLargest(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(largest([5, 2, 8, 1]), 8)
    
    def test_single_element(self):
        self.assertEqual(largest([5]), 5)
    
    def test_reverse_sorted(self):
        self.assertEqual(largest([4, 3, 2, 1]), 4)
    
    def test_empty_raises_error(self):
        with self.assertRaises(ValueError):
            largest([])

if __name__ == '__main__':
    unittest.main()
```

## 💡 Best Practices

1. **Isolate tests** - Each test should be independent
2. **Test edge cases** - Empty, single, duplicates
3. **Clear names** - Describe what's being tested
4. **Assertions** - Use specific assertions
5. **Setup/Teardown** - Use fixtures when needed

---

**Tests ensure code correctness and prevent regressions!** ✅
