def merge(arr, si, mid, ei):
    i = si
    j = mid + 1
    while (i <= mid) and (j <= ei):
        if arr[i] <= arr[j]:
            i += 1
        else:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    return arr


def merge_sort(arr, si, ei):
    """https://takeuforward.org/data-structure/merge-sort-algorithm/"""
    if si >= ei:
        return
    mid = (si + ei) // 2
    merge_sort(arr, si, mid)
    merge_sort(arr, mid + 1, ei)
    return merge(arr, si, mid, ei)


if __name__ == "__main__":
    print(merge_sort([1, 7, 4, 8, 3], 0, 4))
    print(merge_sort([1, 7, 4, 8], 0, 3))