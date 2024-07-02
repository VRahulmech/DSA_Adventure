def leader(arr):
    """https://takeuforward.org/data-structure/leaders-in-an-array/"""
    n = len(arr)
    max_ = arr[-1]
    ans = [arr[-1]]
    for i in range(n-2, -1, -1):
        if arr[i] > max_:
            max_ = arr[i]
            ans.append(arr[i])
    return ans


if __name__ == "__main__":
    print(leader([7, 4, 1, 0]))
    print(leader([22, 12, 3, 0, 6]))

