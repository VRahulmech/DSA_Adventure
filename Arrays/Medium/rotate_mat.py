def rotate(arr):
    """https://takeuforward.org/data-structure/rotate-image-by-90-degree/"""
    n = len(arr)

    for i in range(n):
        for j in range(i):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

    for i in range(n):
        for j in range(n//2):
            arr[i][j], arr[i][n-1-j] = arr[i][n-1-j], arr[i][j]

    return arr


if __name__ == "__main__":
    print(rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))