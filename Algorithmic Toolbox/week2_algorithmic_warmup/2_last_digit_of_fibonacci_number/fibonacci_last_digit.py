# Uses python3
import sys


def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10


# https://www.geeksforgeeks.org/program-find-last-digit-nth-fibonnaci-number/


def get_fibonacci_last_digit(n):
    if n <= 1:
        return n

    a = [0, 1]
    f = [0, 1]

    for _ in range(2, 60):
        sum = a[0] + a[1]
        a[0], a[1] = a[1], sum
        f.append(a[1] % 10)

    return f[n % 60]


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit(n))
