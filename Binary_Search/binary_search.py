class Solution:
    def search(self, nums: list[int], target: int) -> int:
        L = 0
        R = len(nums)-1
        m = (R + L) // 2

        while L <= R:
            mid = (L + R) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                L = mid + 1
            else:
                R = mid - 1

        return -1