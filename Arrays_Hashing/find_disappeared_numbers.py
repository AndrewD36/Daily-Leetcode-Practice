class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        missingNums = []

        numsSet = set(nums)

        for i in range(1, len(nums) + 1):
            if i not in numsSet:
                missingNums.append(i)

        return missingNums