def move_zeroes(arr):
    """https://takeuforward.org/data-structure/move-all-zeros-to-the-end-of-the-array/"""
    n = len(arr)
    j = 0
    while j < n and arr[j] != 0:
        j += 1

    k = j + 1
    while k < n:
        if arr[k] != 0:
            arr[k], arr[j] = arr[j], arr[k]
            j += 1
        k += 1
    return arr


if __name__ == "__main__":
    print(move_zeroes([1, 2, 0, 3, 0, 5]))
    print(move_zeroes([0, 0, 0, 1, 2]))
    print(move_zeroes([1, 2, 3]))

