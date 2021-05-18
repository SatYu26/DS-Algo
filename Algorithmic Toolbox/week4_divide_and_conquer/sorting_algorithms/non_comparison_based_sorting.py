# Non-Comparison Based Sorting Algorithms

def CountSorting(A):
    n = len(A)
    max_n = max(A)
    min_n = min(A)
    m = max_n - min_n + 1

    count = [0]*m

    for i in range(n):
        count[A[i]-min_n] += 1

    for i in range(m):
        for j in range((count[i])):
            print((i + min_n), end=" ")


print(CountSorting([5, 3, 1, 4, 6, 3]))
