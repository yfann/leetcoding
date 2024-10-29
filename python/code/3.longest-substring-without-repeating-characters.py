#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
import math

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if s is empty, return 0
        if not s:
            return 0

        # if s has only one character, return 1
        if len(s) == 1:
            return 1

        # create a dictionary to store the index of each character
        char_dict = {}
        max_len = 0
        start = 0

        for i, char in enumerate(s):
            # if the character is already in the dictionary
            if char in char_dict:
                # update the start index
                start = max(start, char_dict[char] + 1)
            # update the character index
            char_dict[char] = i
            # update the max length
            max_len = max(max_len, i - start + 1)

        return max_len
        
# @lc code=end

