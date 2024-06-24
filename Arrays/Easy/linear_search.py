def linear(arr, num):
    """https://takeuforward.org/data-structure/linear-search-in-c/"""
    for i in arr:
        if i == num:
            return arr.index(i)
    return -1


if __name__ == "__main__":
    print(linear([1, 4, 2, 6, 7], 6))