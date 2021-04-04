def shuffle(self, nums, n):
    return reduce(lambda a, b: a + b, [[nums[i], nums[j]] for i, j in zip(range(0, n), range(n, 2 * n))])