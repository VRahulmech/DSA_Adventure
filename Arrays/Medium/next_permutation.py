def next(arr):
    """https://takeuforward.org/data-structure/next_permutation-find-next-lexicographically-greater-permutation/"""
    n = len(arr)
    ind = -1

    for i in range(n-1, 0, -1):
        if arr[i] > arr[i - 1]:
            ind = i - 1
            break

    if ind != -1:
        for i in range(n-1, ind, -1):
            if arr[ind] < arr[i]:
                arr[ind], arr[i] = arr[i], arr[ind]
                break

    j = ind + 1
    k = n - 1
    while j <= k:
        arr[j], arr[k] = arr[k], arr[j]
        j += 1
        k -= 1
    return arr


if __name__ == "__main__":
    print(next([1, 2, 4, 5, 3, 0, 0]))
    print(next([5, 3, 0, 0]))
    print(next([1, 2, 3]))
