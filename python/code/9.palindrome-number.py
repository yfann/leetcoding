#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 or x>(2**31 - 1):
            return False
        elif x==0:
            return True
        else:
            return x == self.revert(x)
        
    def revert(self, x: int) -> int:
        result=0
        while x!=0:
            result=result*10+x%10
            x=x//10
        return result
        
# @lc code=end

