def remove_dup(arr):
    """https://takeuforward.org/data-structure/remove-duplicates-in-place-from-sorted-array/"""
    i = 0
    n = len(arr)
    for j in range(1, n):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]
    return arr[:i+1]


if __name__ == "__main__":
    print(remove_dup([1, 1, 2, 2, 2]))
    print(remove_dup([1, 1, 2, 3, 3]))
    print(remove_dup([1, 2, 3, 4]))
