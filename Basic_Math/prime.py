import math


def prime(n):
    """https://takeuforward.org/data-structure/check-if-a-number-is-prime-or-not/"""
    sqr = int(math.sqrt(n))
    for i in range(2, sqr + 1):
        if n % i == 0:
            return False

    return True


if __name__ == '__main__':
    print(prime(10))
    print(prime(7))
    print(prime(2))