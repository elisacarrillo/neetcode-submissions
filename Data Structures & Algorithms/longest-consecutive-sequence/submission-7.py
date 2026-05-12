class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        start = 0
        end = 1
        longest_period = 1
        sorted_nums = sorted(set(nums))
        print(sorted_nums)
        while end < len(sorted_nums):
            if (sorted_nums[end - 1] + 1 == sorted_nums[end] ):
                
                if (longest_period <= (end - start)):
                    longest_period = end - start + 1

                
                end = end + 1
                
            else:
                start = start + 1
                end = start + 1
        return longest_period 


        