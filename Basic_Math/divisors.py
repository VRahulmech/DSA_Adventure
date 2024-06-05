import math


def divisors(n):
    """https://takeuforward.org/data-structure/print-all-divisors-of-a-given-number/"""
    sqr = int(math.sqrt(n))
    div = []
    for i in range(1, sqr + 1):
        if n % i == 0:
            div.append(i)
            div.append(n//i)

    return sorted(div)


if __name__ == '__main__':
    print(divisors(10))

