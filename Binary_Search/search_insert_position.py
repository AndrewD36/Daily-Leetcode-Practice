class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        L = 0
        R = len(nums) - 1
        while L <= R:
            m = (L + R) // 2
            if nums[m] == target:
                return m
            if nums[m] > target:
                R = m - 1
            else:
                L = m + 1
        return L