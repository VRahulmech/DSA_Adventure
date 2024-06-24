def appear(arr):
    """https://takeuforward.org/arrays/find-the-number-that-appears-once-and-the-other-numbers-twice/"""
    xor = 0
    for i in arr:
        xor ^= i
    return xor


if __name__ == "__main__":
    print(appear([1, 0, 1, 7, 5, 0, 5]))