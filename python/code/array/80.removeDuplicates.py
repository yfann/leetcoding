def removeDuplicates(nums):
    if len(nums) <= 2:
        return len(nums)
    
    slow = 2  # 下一个要写入的位置
    for fast in range(2, len(nums)):
        if nums[fast] != nums[slow - 2]:
            nums[slow] = nums[fast]
            slow += 1
    return slow