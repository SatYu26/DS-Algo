def decompressRLElist(self, nums):
    return reduce(lambda a, b: a + b, [[nums[i + 1]] * nums[i] for i in range(0, len(nums), 2)])