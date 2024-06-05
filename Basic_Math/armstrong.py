def arm(n):
    """https://takeuforward.org/maths/check-if-a-number-is-armstrong-number-or-not/"""
    dup = n
    sum_ = 0
    while n > 0:
        sum_ += (n % 10)**3
        n //= 10
    if dup == sum_:
        return True
    else:
        return False


if __name__ == "__main__":
    print(arm(151))
    print(arm(153))