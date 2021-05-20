# Uses python3
import sys


def greedy_change(money):
    change = []
    dem = [1, 3, 4]

    while money > 0:
        coin = 0
        for i in dem:
            if i <= money:
                coin = max(coin, i)

        change.append(coin)
        money -= coin
    return change


INF = 100000


def min(x, y):
    if x < y:
        return x
    return y


def coin_change(d, m, k):
    M = [0]*(m+1)

    for j in range(1, m+1):
        minimum = INF

        for i in range(1, k+1):
            if(j >= d[i]):
                minimum = min(minimum, 1+M[j-d[i]])
        M[j] = minimum

    return M[m]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    d = [1, 3, 4]  # denominations
    k = 2  # length of denominations
    print(coin_change(d, m, k))
