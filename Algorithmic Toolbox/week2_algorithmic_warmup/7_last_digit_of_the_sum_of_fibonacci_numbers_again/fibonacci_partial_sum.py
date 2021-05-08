# Uses python3
import sys


def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10


# def fibonacci_mod10(n):

#     previous, current = 0, 1
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     for i in range(n - 1):
#         previous, current \
#             = current, previous + current

#     return (current % 10)

# def fibonacci_sum(from_, to):
#     from_ = from_ % 60
#     to = from_ + (to - from_) % 60
#     sum = 0
#     for i in range(from_, to+1):
#         sum += fibonacci_mod10(i)
#     sum = sum % 10
#     return sum


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


def fibonacci_partial_sum(m, n):
    if n == 0 and m == 0:
        return 0
    if m == 0:
        return fibonacci(n) % 10

    final = fibonacci(n)-fibonacci(m-1)
    return final % 10


if __name__ == '__main__':
    input = sys.stdin.read()
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum(from_, to))
