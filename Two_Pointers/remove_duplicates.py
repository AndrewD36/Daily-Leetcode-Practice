class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        L = 0
        R = 1

        while R < len(nums):
            if nums[L] == nums[R]:
                nums.pop(L)
                continue
            
            L += 1
            R += 1

        return R