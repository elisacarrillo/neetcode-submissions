class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(left, right):
            result = []
            i = j = 0
            while (i < len(left)) and (j < len(right)):
                if (left[i] <= right[j]):
                    result.append(left[i])
                    i = i + 1
                else :
                    result.append(right[j])
                    j = j + 1
            result.extend(left[i:])
            result.extend(right[j:])
            return result


        if len(nums) <= 1:
            return nums

        left_index_end = len(nums)//2
        right_index_start = len(nums) //2 
        return merge(self.sortArray(nums[:left_index_end]),self.sortArray(nums[right_index_start:]))

        
