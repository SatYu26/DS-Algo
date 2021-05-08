# Uses python3
import sys


def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    sum = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10


def fibonacci(n):
    a = [0, 1]
    if n <= 1:
        return n
    else:
        rem = n % 60

        if rem == 0:
            return 0

        for _ in range(2, rem+3):
            sum = a[0] + a[1]
            a[0], a[1] = a[1], sum % 60
        s = a[1] - 1
        return s


def fibonacci_sum(n):
    return fibonacci(n) % 10


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum(n))
