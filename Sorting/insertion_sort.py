def insertion(arr):
    """https://takeuforward.org/data-structure/insertion-sort-algorithm/"""
    n = len(arr)
    for i in range(n-1):
        j = i
        while j >= 0 and arr[j + 1] < arr[j]:
            print(arr)
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j -= 1
    return arr


if __name__ == "__main__":
    print(insertion([1, 4, 7, 5, 2]))
    print(insertion([1, 2, 7, 5]))
