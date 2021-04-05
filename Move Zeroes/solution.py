class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0
        search = False
        while j < len(nums):
            if search:
                if nums[j] != 0:
                    nums[i], nums[j] = nums[j], nums[i]
                    search = False
                    i += 1
                j += 1
            elif nums[i] == 0:
                search = True
            else:
                i += 1
                j += 1