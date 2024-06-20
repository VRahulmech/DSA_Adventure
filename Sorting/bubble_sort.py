def bubble(arr):
    """https://takeuforward.org/data-structure/bubble-sort-algorithm/"""
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == "__main__":
    print(bubble([1, 4, 2, 7, 6]))
    print(bubble([1, 4, 2, 7]))
