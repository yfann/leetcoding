def majorityElement(nums):
    mem={}
    for i in range(len(nums)):
        if nums[i] in mem:
            mem[nums[i]]+=1
        else:
            mem[nums[i]]=1
    for key,value in mem.items():
        if value>len(nums)//2:
            return key
        