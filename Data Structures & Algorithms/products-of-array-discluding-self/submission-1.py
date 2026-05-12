class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        product = math.prod(nums)
        for i, num in enumerate(nums):
            if (num == 0):
                nums[i] = 1
                output.append(int(math.prod(nums)))
                nums[i] = num
            else:
                output.append(int(product/num))
        return output
        

        