# Uses python3
# def calc_fib(n):
#     if (n <= 1):
#         return n

#     return calc_fib(n - 1) + calc_fib(n - 2)


def my_sol(n):
    if (n <= 1):
        return n

    a = [0, 1]

    for i in range(2, n+1):
        sum = a[i-1] + a[i-2]
        a.append(sum)
    return a[n]


n = int(input())
print(my_sol(n))
