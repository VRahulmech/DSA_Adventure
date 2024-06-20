def pri(n):
    """https://takeuforward.org/recursion/print-n-to-1-using-recursion/"""
    if n == 0:
        return
    print(n)
    pri(n-1)
    return


if __name__ == '__main__':
    pri(5)