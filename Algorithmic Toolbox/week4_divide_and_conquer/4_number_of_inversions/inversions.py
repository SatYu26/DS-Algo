import sys


def merge(b, c):

    result = []
    inversions = 0
    while b and c:
        if b[0] <= c[0]:
            result.append(b.pop(0))
        else:
            result.append(c.pop(0))
            inversions += len(b)

    result += b or c
    return result, inversions


def merge_sort(a):

    if len(a) == 1:
        return a, 0

    mid = len(a) // 2
    left, left_inv = merge_sort(a[:mid])
    right, right_inv = merge_sort(a[mid:])

    merged, merged_inv = merge(left, right)
    return merged, merged_inv + left_inv + right_inv


if __name__ == "__main__":
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(merge_sort(a)[1])
