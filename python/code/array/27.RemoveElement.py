def removeElement(arr,element):
    slow=0
    for fast in range(len(arr)):
        if arr[fast]!=element:
            arr[slow]=arr[fast]
            slow+=1
    return slow