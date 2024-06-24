def cons_ones(arr):
    """https://takeuforward.org/data-structure/count-maximum-consecutive-ones-in-the-array/"""
    max_ = 0
    cnt = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            cnt += 1
        else:
            cnt = 0
        max_ = max(max_, cnt)
    return max_


if __name__ == "__main__":
    print(cons_ones([1, 1, 0, 1, 1, 1]))