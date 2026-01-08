class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        triplets = []


        for i in range(0, len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]: 
                continue

            for j in range(i+1, len(nums)-1):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                
                k = -(nums[i] + nums[j])
                if k in nums[j+1:]:
                    triplets.append([nums[i], nums[j], k])

        return triplets
