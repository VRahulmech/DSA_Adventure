def largest(arr, n):
    """https://takeuforward.org/data-structure/find-the-largest-element-in-an-array/"""
    large = arr[0]
    for i in range(1, n):
        if arr[i] > large:
            large = arr[i]
    return large


if __name__ == "__main__":
    print(largest([1, 5, 9, 3, 2], 5))
