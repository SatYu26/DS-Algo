class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        else:
            sum1=sum(nums)
            sum2=2*sum(set(nums))
            return sum2-sum1