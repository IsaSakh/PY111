def fib_recursive(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using recursive algorithm

    :param n: number of item
    :return: Fibonacci number
    """

    if n < 0:
        raise ValueError
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib_recursive(n - 1) + fib_recursive(n - 2)




def fib_iterative(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using iterative algorithm

    :param n: number of item
    :return: Fibonacci number
    """

    if n < 0:
        raise ValueError

    fib_ = [0, 1, 1]
    for i in range(2, n):
        fib_.append(fib_[-1] + fib_[-2])
    return fib_[n]


# if __name__ == '__main__':
#     print(fib_recursive(8))
#     print(fib_iterative(8))