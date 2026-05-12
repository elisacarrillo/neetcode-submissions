class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights) -1
        res = 0
        while start < end:
            curr_container = min(heights[start], heights[end]) * (end - start)
            res = max(curr_container, res)

            if (heights[start] < heights[end]):
                start = start + 1
            else:
                end = end - 1

        return res
        