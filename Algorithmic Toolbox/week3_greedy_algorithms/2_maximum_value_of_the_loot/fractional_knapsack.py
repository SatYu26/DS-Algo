# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    n = len(values)
    V = 0
    B = []
    for j in range(n):
        B.append(values[j]/weights[j])

    for _ in range(n):
        if capacity == 0:
            return V
        index = B.index(max(B))
        a = min(weights[index], capacity)
        V = V + a*(values[index]/weights[index])
        weights[index] = weights[index] - a
        capacity = capacity - a
        weights.pop(index)
        values.pop(index)
        B.pop(index)
    return V


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))
