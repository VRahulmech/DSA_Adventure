def count(n):
    """https://takeuforward.org/data-structure/count-digits-in-a-number/"""

    c = 0
    while n>0:
        c += 1
        n = n//10
    return c


if __name__ == '__main__':
    print(count(2510))