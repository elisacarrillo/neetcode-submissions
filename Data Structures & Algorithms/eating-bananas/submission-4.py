class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours_needed(k):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/k)
            return hours

        lo, hi= 1, max(piles)
        res = hi
        while (lo <= hi):
            mid = (lo + hi) // 2
            if (hours_needed(mid) <= h):
                res = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return res