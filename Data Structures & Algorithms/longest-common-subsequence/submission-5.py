from functools import cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def dfs(i, j):
            if (len(text1) == i or len(text2) == j):
                return 0
            if (text1[i] == text2[j]):
                return 1 + dfs(i+1,j+1)
            return max(dfs(i+1,j), dfs(i, j+1))
        
        return dfs(0,0)