class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        R = k
        total = 0

        for L in range(0, len(arr)-(k-1)):
            if (sum(arr[L:R]) / k) >= threshold:
                total += 1

            R += 1

        return total