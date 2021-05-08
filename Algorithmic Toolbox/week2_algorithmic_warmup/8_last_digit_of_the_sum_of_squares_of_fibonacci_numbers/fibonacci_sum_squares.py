# Uses python3
from sys import stdin


def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    sum = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10


def pisano_num_mod10(n):
    previous, current = 0, 1
    n = n % 60
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        for _ in range(2, n+1):
            previous, current = current, (previous + current) % 60
        return current


if __name__ == '__main__':
    n = int(stdin.read())
    print(pisano_num_mod10(n)*pisano_num_mod10(n+1) % 10)
