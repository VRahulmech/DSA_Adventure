def is_sorted(arr):
    """https://takeuforward.org/data-structure/check-if-an-array-is-sorted/"""
    n = len(arr)
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


if __name__ == "__main__":
    print(is_sorted([1, 5, 9, 3, 2]))
    print(is_sorted([1, 2, 5, 7]))
    print(is_sorted([3, 7, 8, 9]))
    print(is_sorted([1, 8, 4]))