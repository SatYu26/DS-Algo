def numIdenticalPairs(self, nums):
    return sum([int(i != j and nums[i] == nums[j]) for i in range(0, len(nums)) for j in range(i + 1, len(nums))])