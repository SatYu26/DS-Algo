import sys


def max_dot_product(a, b):
    n = len(a)
    a.sort(reverse=True)
    b.sort(reverse=True)
    c = [0]*n
    for i in range(n):
        c[i] = a[i] * b[i]
    return sum(c)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
