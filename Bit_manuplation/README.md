# Bit Manipulation

This directory contains bit manipulation algorithms and techniques.

## 📚 About Bit Manipulation

Bit manipulation involves performing operations on individual bits for efficient computation and optimization.

## 🎯 Basic Operations

```python
a & b    # AND - Both bits must be 1
a | b    # OR - At least one bit is 1
a ^ b    # XOR - Bits must be different
~a       # NOT - Invert all bits
a << n   # Left shift - Multiply by 2^n
a >> n   # Right shift - Divide by 2^n
```

## 💡 Useful Tricks

- Check if power of 2: `(n & (n-1)) == 0`
- Count set bits: Use Brian Kernighan's algorithm
- Check if bit set: `n & (1 << i)`
- Set bit: `n | (1 << i)`
- Clear bit: `n & ~(1 << i)`

---

**Bit manipulation optimizes solutions and saves memory!** ⚡
