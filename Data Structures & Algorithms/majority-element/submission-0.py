class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq_map = {}
        res = 0
        for num in nums:
            if num in freq_map:
                freq_map[num] = freq_map[num] + 1
            else:
                freq_map[num] = 1
        res = max(freq_map, key = freq_map.get)
        return res
        