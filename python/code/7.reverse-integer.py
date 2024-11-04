#
# @lc app=leetcode id=7 lang=python
#
# [7] Reverse Integer
#

# @lc code=start
class Solution(object):
    def reverse(self, x):
        li=[]
        pos=1
        if x==0:
            return 0
        if x<0:
            pos=-1
            x=-x
        while x!=0:
          mod=x%10
          x=x//10
          li.append(mod)
        sum=0
        l=len(li)
        for i in li:
          l-=1
          sum+=i*(10**l)
        result=sum*pos
        if result<-(2**31) or result>(2**31-1):
          return 0
        else:
          return result

        
# @lc code=end

