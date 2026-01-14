class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = R = 0
        res = 0
        substring = set()

        while R < len(s):
            if s[R] in substring:
                substring.remove(s[L])
                L += 1
                continue

            substring.add(s[R])
            R += 1

            if len(substring) > res:
                res = len(substring)

        return res