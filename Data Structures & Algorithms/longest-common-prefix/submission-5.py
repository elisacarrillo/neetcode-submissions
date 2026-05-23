class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        print(strs)
        start = strs[0]
        end = strs[-1]
        res = ""
        for i, char in enumerate(start):
            if (start[i] != end[i]):
                return res
            res += char
        return res