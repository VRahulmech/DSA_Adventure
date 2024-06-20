def reverse(arr, start, end):
    """https://takeuforward.org/data-structure/reverse-a-given-array/"""
    if start >= end:
        return arr
    arr[start], arr[end] = arr[end], arr[start]
    return reverse(arr, start + 1, end - 1)


if __name__ == '__main__':
    print(reverse([1, 2, 3, 4], 0, 3))
    print(reverse([1, 2, 3], 0, 2))