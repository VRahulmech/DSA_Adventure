def stock(arr):
    """https://takeuforward.org/data-structure/stock-buy-and-sell/"""
    min_ = arr[0]
    n = len(arr)
    profit = 0
    first = arr[0]
    second = arr[0]

    for i in range(1, n):
        if arr[i] - min_ > profit:
            profit = arr[i] - min_
            first = min_
            second = arr[i]
        if min_ > arr[i]:
            min_ = arr[i]

    return profit, [first, second]


if __name__ == "__main__":
    print(stock([7, 1, 5, 3, 6, 4]))