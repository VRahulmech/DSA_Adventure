def sum_(n):
    """https://takeuforward.org/data-structure/sum-of-first-n-natural-numbers/"""
    if n == 1:
        return 1
    return n + sum_(n-1)


if __name__ == '__main__':
    print(sum_(10))
    print(sum_(100))