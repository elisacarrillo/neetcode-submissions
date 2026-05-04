class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            what_we_looking_for = target - num 
            if what_we_looking_for in seen:
                return [seen[what_we_looking_for], i]

            seen[num] = i
               


        