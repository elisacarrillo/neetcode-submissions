class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ind1 = 0
        ind2 = len(numbers) - 1
        while ind2 > ind1:

            subtract =  numbers[ind2] + numbers[ind1]
            if subtract > target:
                ind2 -= 1
            elif subtract < target:
                ind1 += 1
            else:
                return [ind1 + 1, ind2 + 1]