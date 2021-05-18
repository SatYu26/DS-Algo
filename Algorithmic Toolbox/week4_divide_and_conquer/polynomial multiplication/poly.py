def multiplypoly_naive(A, B, n):
    product = []
    for i in range(2*n-2):
        product[i] = 0

    for i in range(n-1):
        for j in range(n-1):
            product[i+j] += A[i] * B[j]

    return product
