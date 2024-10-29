# Remove Duplicates from Sorted Array

def removeDup(arr):
    j=0
    for i in range(1,len(arr)):
        if arr[j]!=arr[i]:
            j+=1
            arr[j]=arr[i]
    if (j+1)<len(arr):
        del arr[j+1:]
    print(arr)



# a=[1,2,3,3,3,4,4,5]
# removeDup(a)