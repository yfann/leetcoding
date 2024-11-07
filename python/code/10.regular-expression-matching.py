#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(s)>20 or len(p)>20:
            return False
        if '*' not in p and '.' not in p:
            return s == p

        
        
# @lc code=end

