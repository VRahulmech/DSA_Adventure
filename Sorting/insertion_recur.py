def insertion(arr, j, n):
    if j >= n:
        return arr
    i = j
    while i > 0 and arr[i] < arr[i - 1]:
        arr[i], arr[i - 1] = arr[i - 1], arr[i]
        i -= 1
    return insertion(arr, j + 1, n)


if __name__ == "__main__":
    print(insertion([1, 4, 7, 5, 2], 1, 5))
    print(insertion([1, 2, 7, 5], 1, 4))

