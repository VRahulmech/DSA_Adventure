def sort012(arr):
    """https://takeuforward.org/data-structure/sort-an-array-of-0s-1s-and-2s/"""
    left = 0
    right = len(arr) - 1
    mid = 0
    while mid < right:
        if arr[mid] == 0:
            arr[left], arr[mid] = arr[mid], arr[left]
            left += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        elif arr[mid] == 2:
            arr[mid], arr[right] = arr[right], arr[mid]
            right -= 1
    return arr


if __name__ == "__main__":
    print(sort012([2, 1, 0]))
    print(sort012([1, 0, 2, 1, 0]))
