#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        start,end=0,0
        def expand_around_center(left: int,right: int)->None:
            nonlocal start,end
            while left>=0 and right < len(s) and s[left]==s[right]:
                left-=1
                right+=1
            if right-left-1>end-start:
                start,end=left+1,right-1
        for i in range(len(s)):
            expand_around_center(i,i)
            expand_around_center(i, i + 1)
        return s[start:end+1]


# @lc code=end

