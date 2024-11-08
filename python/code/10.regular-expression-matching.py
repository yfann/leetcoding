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
        current=0

        for c in p:
            if current>=len(s):
                return False
            if c=='.':
                current+=1
                continue
            elif c=='*':
                pass
            else:
                if c==s[current]:
                    current+=1
                    continue
                else:
                    return False


            
            

        
        
# @lc code=end

