"""
Linear Search Implementation.

Linear search sequentially checks each element in a list
until the target value is found or the list ends.

Time Complexity:
    Best Case: O(1)
    Average Case: O(n)
    Worst Case: O(n)

Space Complexity:
    O(1)
"""


def linear_search(numbers: list[int], target: int) -> int:
    """
    Search for a target value in a list.

    Args:
        numbers: List of integers to search.
        target: Value to find.

    Returns:
        Index of the target if found, otherwise -1.
    """
    for index, value in enumerate(numbers):
        if value == target:
            return index

    return -1


def main() -> None:
    """
    Execute linear search example.
    """
    numbers = [1, 2, 3, 4, 5]
    target = 3

    result = linear_search(numbers, target)

    if result != -1:
        print(f"Target found at index {result}")
    else:
        print("Target not found")


if __name__ == "__main__":
    main()