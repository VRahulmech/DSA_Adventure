def reverse(arr, i, j):
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return arr


def rotate(arr, d):
    """https://takeuforward.org/data-structure/rotate-array-by-k-elements/"""
    n = len(arr)
    if d >= n:
        d = d % n
    reverse(arr, 0, d-1)
    reverse(arr, d, n-1)
    reverse(arr, 0, n-1)
    return arr


if __name__ == "__main__":
    print(rotate([1, 2, 3, 4], 2))
    print(rotate([1, 2, 4, 8, 9], 3))
    print(rotate([1, 2, 4], 5))


