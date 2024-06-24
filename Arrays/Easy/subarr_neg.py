def subarr(arr, s):
    """https://takeuforward.org/arrays/longest-subarray-with-sum-k-postives-and-negatives/"""
    j = 0
    sum_ = 0
    max_ = 0
    hash = {}
    for i in range(len(arr)):

        print(i, sum_, arr, hash, max_, s - sum_)
        sum_ += arr[i]
        if s - sum_ in hash:
            print("if")
            max_ = max(max_, i - hash[s - sum_] + 2)
        elif sum_ not in hash:
            print('else')
            hash[sum_] = i
    return max_


if __name__ == "__main__":
    print(subarr([1, -1, 1], 1))
    print(subarr([1, -1, 1, 1, -1, -1, 1], 1))
