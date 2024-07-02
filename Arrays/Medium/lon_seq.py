def long(arr):
    """https://takeuforward.org/data-structure/longest-consecutive-sequence-in-an-array/"""
    
    n = len(arr)
    s = set()
    for i in range(n):
        s.add(arr[i])

    longest = 1
    for i in s:
        if i - 1 not in s:
            cnt = 1
            j = i
            while j + 1 in s:
                cnt += 1
                j += 1

        longest = max(longest, cnt)

    return longest


if __name__ == "__main__":
    print(long([1, 2, 6, 5, 43, 4, 8, 3]))

