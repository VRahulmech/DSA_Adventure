def union(arr1, arr2):
    """https://takeuforward.org/data-structure/union-of-two-sorted-arrays/"""
    i = 0
    j = 0
    arr = []
    while (i < len(arr1)) and (j < len(arr2)):
        if arr1[i] <= arr2[j]:
            if len(arr) == 0:
                arr.append(arr1[i])
                i += 1
            elif arr1[i] != arr[-1]:
                arr.append(arr1[i])
                i += 1
            else:
                i += 1

        elif arr1[i] > arr2[j]:
            if len(arr) == 0:
                arr.append(arr2[j])
                j += 1
            elif arr2[j] != arr[-1]:
                arr.append(arr2[j])
                j += 1
            else:
                j += 1

    while i < len(arr1):
        if arr1[i] != arr[-1]:
            arr.append(arr1[i])
            i += 1
        else:
            i += 1

    while j < len(arr2):
        if arr2[j] != arr[-1]:
            arr.append(arr2[j])
            j += 1
        else:
            j += 1

    return arr


if __name__ == "__main__":
    print(union([1, 1, 2, 3], [2, 2, 3, 4]))