def check_pal(n):
    """https://takeuforward.org/data-structure/check-if-a-number-is-palindrome-or-not/"""
    dup = n
    rev_num = 0

    while n > 0:
        rev_num = rev_num*10 + n%10
        n = n//10

    if rev_num == dup:
        return True

    else:
        return False


if __name__ == "__main__":
    print(check_pal(424))
    print(check_pal(423))