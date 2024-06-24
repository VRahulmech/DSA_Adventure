def missing_number(nums) -> int:
    """https://takeuforward.org/arrays/find-the-missing-number-in-an-array/"""
    n = len(nums)
    hash = [0] * (n + 1)
    for i in nums:
        hash[i] += 1
    for j in hash:
        if j == 0:
            return hash.index(0)
    return -1


def missing_num(nums):
    xor1 = xor2 = 0
    for i in range(len(nums)):
        xor1 = xor1 ^ (i + 1)
        xor2 = xor2 ^ nums[i]
    return xor1 ^ xor2


def missing(nums):
    n = len(nums)
    sum_ = sum(nums)
    act = n * (n + 1)/2
    return act - sum_


if __name__ == "__main__":
    print(missing_number([0, 4, 2, 3]))
    print(missing_number([0, 4, 2, 3, 1]))
    print(missing_num([0, 4, 2, 3]))
    print(missing_num([0, 4, 2, 3, 1]))
    print(missing([0, 4, 2, 3]))
    print(missing([0, 4, 2, 3, 1]))