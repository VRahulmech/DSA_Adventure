def selection(arr):
    """https://takeuforward.org/sorting/selection-sort-algorithm/"""
    n = len(arr)
    for i in range(n-1):
        min_ind = i
        for j in range(i, n-1):
            if arr[j] < arr[min_ind]:
                min_ind = j
        arr[min_ind], arr[i] = arr[i], arr[min_ind]
    return arr

# O(T) = N*N


if __name__ == "__main__":
    print(selection([1, 4, 3, 2, 7]))
    print(selection([1, 4, 3, 2, 7, 8]))