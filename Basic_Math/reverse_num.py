def rev(n):
    """https://takeuforward.org/maths/reverse-digits-of-a-number"""
    num = 0
    while n > 0:
        rem = n%10
        num = num*10 + rem
        n //= 10
    return num


if __name__ == '__main__':
    print(rev(251))
    print(rev(10))