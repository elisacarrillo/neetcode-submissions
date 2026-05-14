class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums_sorted = sorted(nums)
   
        for i in range(len(nums)):
            if (i > 0 and i < len(nums) and nums_sorted[i] == nums_sorted[i - 1]):
                continue
            # print(i)
            ptr1 = i + 1
            ptr2 = len(nums) - 1
            while ptr2 > ptr1 and ptr1 < len(nums) and ptr2 >= 0:
            
                sum_total = nums_sorted[ptr1] + nums_sorted[ptr2] + nums_sorted[i]
                # print(f"{ptr1}, {ptr2}, {i}, {sum_total}")
                if sum_total > 0:
                    ptr2 -= 1 
                       
                elif sum_total < 0:
                    ptr1 += 1
                    
                else:
                    res.append([nums_sorted[ptr1], nums_sorted[ptr2], nums_sorted[i]])
                    ptr1 += 1
                    ptr2 -= 1
                    while (ptr1 < len(nums) and nums_sorted[ptr1] == nums_sorted[ptr1 - 1]):
                        ptr1 = ptr1 + 1
                    while (ptr2 > 0 and nums_sorted[ptr2] == nums_sorted[ptr2+1]):
                        ptr2 = ptr2 - 1
                
                
                
                
          

        return res

        