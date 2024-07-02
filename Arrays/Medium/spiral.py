def spiral(arr):
    """https://takeuforward.org/data-structure/spiral-traversal-of-matrix/"""
    top = 0
    left = 0
    bottom = len(arr) - 1
    right = len(arr[0]) - 1

    while (top <= bottom) and (left <= right):
        for i in range(left, right + 1):
            print(arr[top][i], end = " ")
        top += 1

        for j in range(top, bottom + 1):
            print(arr[j][right], end=" ")
        right -= 1

        if top <= bottom:
            for k in range(right, left-1, -1):
                print(arr[bottom][k], end=" ")
            bottom -= 1

        if left <= right:
            for l in range(bottom, top - 1, -1):
                print(arr[l][left], end = " ")
            left += 1


if __name__ == "__main__":
    spiral([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

