class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        l, r = 0, len(people) - 1
        res = 0

        while (l <= r):
            cap = limit - people[r]
            res = res + 1
            r = r - 1
            if (l <= r and cap >= people[l]):
                l = l + 1

        return res