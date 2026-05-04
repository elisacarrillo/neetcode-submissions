class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 1
        longest_patt = 0
        if (j >= len(s)):
            longest_patt = len(s)
        while i < j and j < len(s) + 1:
            current_check = s[i:j]
            print(current_check)
            current_check_set = set(current_check)
            unique_str_bool = len(current_check) == len(current_check_set)
            if (unique_str_bool and (j-i) > longest_patt ):
                longest_patt = j - i
                print(longest_patt)
            if (unique_str_bool):
                print('here?')
                j = j + 1
            else:
                i = i + 1
                
        return longest_patt
                
