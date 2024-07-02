def alter(arr):
    """https://takeuforward.org/arrays/rearrange-array-elements-by-sign/"""
    pos = 0
    neg = 1
    out = [0] * len(arr)
    for i in arr:
        if i > 0:
            out[pos] = i
            pos += 2
        else:
            out[neg] = i
            neg += 2
    return out


if __name__ == "__main__":
    print(alter([1, 2, -1, -2]))
    print(alter([1, 2, -1, -2, -3, 3]))
