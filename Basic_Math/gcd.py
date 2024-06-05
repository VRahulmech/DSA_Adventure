def gcd(m, n):
    """https://takeuforward.org/data-structure/find-gcd-of-two-numbers/"""
    while m > 0 and n > 0:
        if m > n:
            m = m % n
        else:
            n = n % m

    if m == 0:
        return n
    else:
        return m


if __name__ == "__main__":
    print(gcd(5, 10))
    print(gcd(12, 18))
    print(gcd(2, 3))

