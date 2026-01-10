class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        L = 0
        R = len(people) - 1
        sumBoats = 0

        while L <= R:
            if people[L] + people[R] <= limit:
                sumBoats += 1
                L += 1
                R -= 1
            else:
                sumBoats += 1
                R -= 1

        return sumBoats