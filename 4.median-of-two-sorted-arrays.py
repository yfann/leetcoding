#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
import math

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m=len(nums1)
        n=len(nums2)
        carry,out=divmod(m+n,2) 
        
        medlist=[0]*(carry+1)

        l1=l2=0

        while l1+l2<len(medlist):
            if l1==m:
                medlist[l1+l2]=nums2[l2]
                l2+=1
                continue
            
            if l2==n:
                medlist[l1+l2]=nums1[l1]
                l1+=1
                continue


            if nums1[l1]<nums2[l2]:
                medlist[l1+l2]=nums1[l1]
                l1+=1
            else:
                medlist[l1+l2]=nums2[l2]
                l2+=1
                
        result=0
        if out!=0:
            result=medlist[carry]
        else:
            result=(medlist[carry]+medlist[carry-1])/2

        return result

                


# @lc code=end
