class Solution:
    def mySqrt(self, x: int) -> int:
        L = 0
        R = x
        res = 0

        while L <= R:
            m = L + (R - L) // 2
            if m * m > x:
                R = m - 1
            elif m * m < x:
                L = m + 1
                res = m
            else:
                return m

        return res