def matrix(arr):
    """https://takeuforward.org/data-structure/set-matrix-zero/"""
    m = len(arr)
    n = len(arr[0])
    col0 = None
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 0:
                arr[i][0] = 0

                if j != 0:
                    arr[0][j] = 0
                else:
                    col0 = 0

    for i in range(1, m):
        for j in range(1, n):
            if arr[i][j] != 0:
                if arr[i][0] == 0 or arr[0][j] == 0:
                    arr[i][j] = 0

    if arr[0][0] == 0:
        for i in range(n):
            arr[0][i] = 0

    if col0 == 0:
        for i in range(m):
            arr[i][0] = 0

    return arr


if __name__ == "__main__":
    print(matrix([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
    print(matrix([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))




