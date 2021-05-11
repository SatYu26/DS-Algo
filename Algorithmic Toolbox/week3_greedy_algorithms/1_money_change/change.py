# Uses python3
import sys


def get_change(m):
    ten = int(m / 10)
    five = int((m % 10) / 5)
    one = ((m % 10) % 5)

    m = ten + five + one
    return m


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
