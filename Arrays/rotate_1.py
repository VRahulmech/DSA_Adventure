def rotate(arr):
    """https://takeuforward.org/data-structure/left-rotate-the-array-by-one/"""
    temp = arr[0]
    n = len(arr)
    for j in range(1, n):
        arr[j - 1] = arr[j]
    arr[n - 1] = temp
    return arr


if __name__ == "__main__":
    print(rotate([1, 2, 3, 4]))
    print(rotate([1, 2, 5, 9, 8]))
    print(rotate([1]))
