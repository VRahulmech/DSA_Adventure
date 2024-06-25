def max_sum(arr):
    """https://takeuforward.org/data-structure/kadanes-algorithm-maximum-subarray-sum-in-an-array/"""
    """Kadane's Algorithm"""
    sum_ = 0
    max_ = 0
    n = len(arr)

    for i in range(n):
        sum_ += arr[i]
        if sum_ < 0:
            sum_ = 0
        elif sum_ > max_:
            max_ = sum_

    return max_


if __name__ == "__main__":
    print(max_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))