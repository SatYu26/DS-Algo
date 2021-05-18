

def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def quicksort(a, l, r):
    if l >= r:
        return

    m = partition2(a, l, r)
    quicksort(a, l, m - 1)
    quicksort(a, m + 1, r)
