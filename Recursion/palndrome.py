def palindrome(n, i, rev=0):
    """https://takeuforward.org/data-structure/check-if-the-given-string-is-palindrome-or-not/"""
    if i <= 0:
        if n == rev:
            return True
        else:
            return False
    rev = (rev * 10) + (i % 10)
    i = i//10
    return palindrome(n, i, rev)


if __name__ == '__main__':
    print(palindrome(121, 121))
    print(palindrome(122, 122))