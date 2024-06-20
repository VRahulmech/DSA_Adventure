def pri(n):
    """https://takeuforward.org/recursion/print-1-to-n-using-recursion/"""
    if n == 0:
        return
    pri(n-1)
    print(n)
    return


if __name__ == '__main__':
    pri(5)