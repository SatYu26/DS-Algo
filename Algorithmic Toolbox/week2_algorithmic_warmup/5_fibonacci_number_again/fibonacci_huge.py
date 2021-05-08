# Uses python3
import sys


def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


# https://www.geeksforgeeks.org/fibonacci-number-modulo-m-and-pisano-period/


def get_fibonacci_huge(n, m):

    n = n % pisanoPeriod(m)

    if n <= 1:
        return n

    a = [0, 1]
    for _ in range(n-1):
        sum = a[0] + a[1]
        a[0], a[1] = a[1], sum

    return a[1] % m


def pisanoPeriod(m):
    previous, current = 0, 1
    for i in range(0, m * m):
        previous, current = current, (previous + current) % m
        # A Pisano Period starts with 01
        if (previous == 0 and current == 1):
            return i + 1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n, m))
