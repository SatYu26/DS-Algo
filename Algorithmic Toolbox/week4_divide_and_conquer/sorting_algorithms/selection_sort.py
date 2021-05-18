def selection_sort(A):
    n = len(A)
    for i in range(n):
        minIndex = i

        for j in range(i+1, n):

            if A[j] < A[minIndex]:
                minIndex = j
        A[i], A[minIndex] = A[minIndex], A[i]
    return A


print(selection_sort([5, 3, 1, 4, 6]))
