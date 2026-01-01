class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        numsSet = set(nums)

        return len(numsSet) != len(nums)