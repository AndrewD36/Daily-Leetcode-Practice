class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seenNums = {}

        for i, num in enumerate(nums):
            jnum = target - num
            if jnum in seenNums.keys():
                iindex = seenNums.get(jnum)
                jindex = i
                break
            else:
                seenNums[num] = i

        return [iindex, jindex]