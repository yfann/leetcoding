

def removeDuplicates(arr):
    slow=0
    for fast in range(len(arr)):
        if arr[fast]!=arr[slow]:
            slow +=1
            arr[slow]=arr[fast]
    return slow+1