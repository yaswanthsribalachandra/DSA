"""
Binary Search Implementation.

Binary search efficiently finds a target value in a sorted list
by repeatedly dividing the search space in half.

Time Complexity:
    O(log n)

Space Complexity:
    O(1)
"""


def binary_search(numbers: list[int], target: int) -> int:
    """
    Search for a target value in a sorted list.

    Args:
        numbers: Sorted list of integers.
        target: Value to search for.

    Returns:
        Index of the target if found, otherwise -1.
    """
    left = 0
    right = len(numbers) - 1

    while left <= right:
        middle = (left + right) // 2

        if numbers[middle] == target:
            return middle

        if numbers[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1


def main() -> None:
    """
    Execute binary search example.
    """
    numbers = [10, 20, 30, 40, 50, 60, 70]
    target = 50

    result = binary_search(numbers, target)

    if result != -1:
        print(f"Target found at index {result}")
    else:
        print("Target not found")


if __name__ == "__main__":
    main()