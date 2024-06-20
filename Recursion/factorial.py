def fact(n):
    """https://takeuforward.org/data-structure/factorial-of-a-number-iterative-and-recursive/"""
    if n == 0:
        return 1
    return n * fact(n-1)


if __name__ == '__main__':
    print(fact(3))
    print(fact(6))