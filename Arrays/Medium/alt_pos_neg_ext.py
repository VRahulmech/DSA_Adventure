def alt(arr):
    pos = []
    neg = []
    for i in arr:
        if i > 0:
            pos.append(i)
        else:
            neg.append(i)

    np = len(pos)
    nq = len(neg)

    p = 0
    if np <= nq:
        for i in range(np):
            arr[p] = pos[i]
            arr[p + 1] = neg[i]
            p += 2
        for j in range(np, nq):
            arr[p] = neg[j]
            p += 1

    else:
        for i in range(nq):
            arr[p] = pos[i]
            arr[p + 1] = neg[i]
            p += 2
        for j in range(nq, np):
            arr[p] = pos[j]
            p += 1

    return arr


if __name__ == "__main__":
    print(alt([1, 2, -1, -2, -6, 7, 8, 9, -2, -5, -9, -4]))
    print(alt([1, 2, -1, -2, -3, 3, 4, 5]))






