class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s1_sorted = sorted(s1)
        # s2_sorted = sorted(s2)
        # print(s1_sorted)
        # print(s2_sorted)
        len_s1 = len(s1)

        for i, char in enumerate(s2):
            
            if (sorted(s2[i:i + len_s1]) == sorted(s1)):
                return True
        return False
