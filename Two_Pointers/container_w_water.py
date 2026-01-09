class Solution:
    def maxArea(self, heights: list[int]) -> int:
        L = 0
        R = len(heights) - 1
        area = 0

        while L < R:
            if area < min(heights[L], heights[R]) * (R - L):
                area = min(heights[L], heights[R]) * (R - L)
            if heights[L] <= heights[R]:
                L += 1
            else:
                R -= 1

        return area
