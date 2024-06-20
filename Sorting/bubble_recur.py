def bubble(arr, si, ei):
    if si >= ei:
        return arr
    for i in range(si, ei - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return bubble(arr, si, ei - 1)


if __name__ == "__main__":
    print(bubble([1, 4, 2, 7, 6], 0, 4))
    print(bubble([1, 4, 2, 7], 0, 3))
