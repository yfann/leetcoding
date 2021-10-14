#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
import math

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = [0]*128

        res=l=r=0
        
        while r<len(s):
            chars[ord(s[r])]+=1
            while chars[ord(s[r])]>1:
                chars[ord(s[l])]-=1
                l+=1
            res=max(res,r-l+1)
            r+=1

        return res
        
# @lc code=end

