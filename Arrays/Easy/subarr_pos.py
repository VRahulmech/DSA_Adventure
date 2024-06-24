def subarr(arr, num):
    """https://takeuforward.org/data-structure/longest-subarray-with-given-sum-k/"""
    i = j = 0
    sum_ = 0
    max_ = 0
    n = len(arr)
    while j < n:
        sum_ += arr[j]
        while (sum_ > num) and (i < j):
            sum_ -= arr[i]
            i += 1
        if sum_ == num:
            max_ = max(max_, j - i + 1)
            sum_ = 0
            j += 1
        if sum_ < num:
            j += 1
    return max_


if __name__ == "__main__":
    print(subarr([1, 2, 3, 4, 1, 1, 1], 3))