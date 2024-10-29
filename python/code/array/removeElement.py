def removeElement(arr,element):
    j=0
    for i in range(len(arr)):
        if arr[i]==element:
            continue
        arr[j]=arr[i]
        j+=1
    del arr[j:]
    print(arr)
    return j


# a=[1,2,3,3,4,5]
# removeElement(a,3)