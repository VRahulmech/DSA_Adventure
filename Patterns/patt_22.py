def pat(n):
    for i in range(n):
        for j in range(n):
            print(max(n - i, n - j), end=" ")
        for k in range(1, n):
            print(max(k + 1, n - i), end=" ")
        print()
    for p in range(n-1):
        for m in range(n):
            print(max(p + 2, n - m), end=" ")
        for q in range(n - 1):
            print(max(p + 2, q + 2), end=" ")
        print()


if __name__ == '__main__':
    pat(4)
