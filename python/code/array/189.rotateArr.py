
def rotateArr(arr,k):
    n=len(arr)
    k%=n
    def reverse(arr,i,j):
        while i<j:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j-=1
    reverse(arr,0,n-1)
    reverse(arr,0,k-1)
    reverse(arr,k,n-1)