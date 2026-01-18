class Solution:
    def guessNumber(self, n: int) -> int:
        L = 1
        R = n
        while True:
            m = (L + R) // 2
            res = guess(m)
            if res > 0:
                L = m + 1
            elif res < 0:
                R = m - 1
            else:
                return m