class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        longest = 0
        seen = set()
        for j in range(len(s)):
            while s[j] in seen:
                seen.remove(s[i])
                i += 1
            seen.add(s[j])
            longest = max(longest, j - i + 1)
        # while i < j and j < len(s) + 1:
        #     current_check = s[i:j]
        #     current_check_set = set(current_check)
        #     unique_str_bool = len(current_check) == len(current_check_set)
        #     if (unique_str_bool and (j-i) > longest_patt ):
        #         longest_patt = j - i
        #     if (unique_str_bool):
        #         j = j + 1
        #     else:
        #         i = i + 1
                
        return longest
                
