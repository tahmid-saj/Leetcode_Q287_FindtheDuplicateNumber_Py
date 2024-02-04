class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            j = nums[i] - 1
            if nums[j] != nums[i]: nums[i], nums[j] = nums[j], nums[i]
            else: i += 1
        
        for i in range(0, len(nums)):
            if nums[i] != i + 1: return nums[i]

        return -1
