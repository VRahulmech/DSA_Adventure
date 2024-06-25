def maj_ele(arr):
    """https://takeuforward.org/data-structure/find-the-majority-element-that-occurs-more-than-n-2-times/"""
    """Moore's voting algorithm"""
    n = len(arr)
    prev = arr[0]
    count = 1

    for i in range(1, n):
        if count == 0:
            prev = arr[i]
            count = 1
        elif arr[i] == prev:
            count += 1
        elif arr[i] != prev:
            count -= 1

    c = 0
    for j in range(n):
        if arr[j] == prev:
            c += 1
    if c > n//2:
        return prev
    else:
        return -1


if __name__ == "__main__":
    print(maj_ele([2, 2, 1, 1, 1, 2, 2]))
    print(maj_ele([2, 2, 1, 1, 1, 3, 3]))
    print(maj_ele([2, 5, 5, 2, 5, 1, 1, 1, 5, 5, 3, 3, 5, 5, 5]))