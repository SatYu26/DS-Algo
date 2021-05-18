import random
import sys


def partition2(a, left, right):
    pivot = a[left]
    j = left
    for i in range(left + 1, right + 1):
        if a[i] <= pivot:
            j += 1
            a[i], a[j] = a[j], a[i]

    pivot, a[j] = a[j], pivot
    return j


def partition3(a, left, right):
    pivot = a[left]
    i = left
    lt = left
    gt = right
    while i <= gt:
        if a[i] < pivot:
            a[i], a[lt] = a[lt], a[i]
            lt += 1
            i += 1
        elif a[i] > pivot:
            a[i], a[gt] = a[gt], a[i]
            gt -= 1
        else:
            i += 1

    return lt, gt


def randomized_quick_sort(a, left, right):
    if left >= right:
        return

    random_pivot = random.randint(left, right)
    a[left], a[random_pivot] = a[random_pivot], a[left]

    mid1, mid2 = partition3(a, left, right)
    randomized_quick_sort(a, left, mid1 - 1)
    randomized_quick_sort(a, mid2 + 1, right)


if __name__ == "__main__":
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=" ")
