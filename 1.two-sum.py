#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx1,s1 in enumerate(nums):
            for idx2,s2 in enumerate(nums):
                if idx1!=idx2 and (s1+s2)==target:
                    return [idx1,idx2]

        
# @lc code=end


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[j] == target - nums[i]:
#                     return [i, j]