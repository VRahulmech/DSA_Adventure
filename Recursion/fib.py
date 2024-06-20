def fib(n):
    """https://takeuforward.org/arrays/print-fibonacci-series-up-to-nth-term/"""
    if n == 0 or n == 1:
        return 1
    return fib(n-1) + fib(n-2)


if __name__ == "__main__":
    print(fib(2))
    print(fib(4))
