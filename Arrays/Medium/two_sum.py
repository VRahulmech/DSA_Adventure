def two_sum(arr, num):
    """https://takeuforward.org/data-structure/two-sum-check-if-a-pair-with-given-sum-exists-in-array/"""
    arr.sort()
    left = 0
    right = len(arr) - 1
    while left < right:
        sum_ = arr[left] + arr[right]
        if sum_ == num:
            return True
        elif sum_ < num:
            left += 1
        else:
            right -= 1
    return False


def two_sum_ind(arr, num):
    """https://takeuforward.org/data-structure/two-sum-check-if-a-pair-with-given-sum-exists-in-array/"""
    hash ={}
    sum_ = 0
    for i in range(len(arr)):
        if num - arr[i] in hash:
            return (hash[num - arr[i]], i)
        else:
            hash[arr[i]] = i
    return -1


if __name__ == "__main__":
    print(two_sum([1, 5, 2], 3))
    print(two_sum_ind([1, 5, 2], 3))
