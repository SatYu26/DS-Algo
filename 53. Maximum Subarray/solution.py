class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSubarray=-math.inf
        for i in range(len(nums)):
            currentSubarray=0
            for j in range(i,len(nums)):
                currentSubarray += nums[j]
                maxSubarray=max(maxSubarray, currentSubarray)
        return maxSubarray


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentSubarray=maxSubarray=nums[0]
        for num in nums[1:]:
            currentSubarray = max(num, currentSubarray+num)
            maxSubarray=max(currentSubarray, maxSubarray)
        return maxSubarray



