def kadane(arr):
    """https://takeuforward.org/data-structure/kadanes-algorithm-maximum-subarray-sum-in-an-array/"""
    sum_ = 0
    max_ = 0
    n = len(arr)

    for i in range(n):
        if sum_ == 0:
            start = i
        sum_ += arr[i]
        if sum_ < 0:
            sum_ = 0
        elif sum_ > max_:
            max_ = sum_
            start_ind = start
            end_ind = i
    return max_, arr[start_ind:end_ind + 1]


if __name__ == "__main__":
    print(kadane([-2, 1, -3, 4, -1, 2, 1, -5, 4]))