def print2largest(arr, n):
    """https://takeuforward.org/data-structure/find-second-smallest-and-second-largest-element-in-an-array/"""
    large = arr[0]
    second = -1
    for i in range(1, n):
        if arr[i] > large:
            second = large
            large = arr[i]
        elif second < arr[i] < large:
            second = arr[i]
    return second


if __name__ == "__main__":
    print(print2largest([1, 5, 9, 3, 2], 5))
