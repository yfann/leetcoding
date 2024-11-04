#
# @lc app=leetcode id=6 lang=python
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution(object):
    def convert(self, s, numRows):
        if numRows==1 or numRows>=len(s):
            return s
        list=['' for _ in range(numRows)]
        curr=0
        forward=True
        for p in s:
            list[curr]+=p
            if curr+1==numRows:
                forward=False
            elif curr==0:
                forward=True
            curr+=1 if forward else -1
        return ''.join(list)


        
# @lc code=end

