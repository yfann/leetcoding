
def plusone(arr):
    one = 1
    for i in range(len(arr)-1,-1,-1):
        sum = arr[i]+one
        one = sum // 10
        arr[i] = sum % 10
    
    if one > 0:
        arr.insert(0,one)
    print(arr)

# a=[1,2,3,4,5]
# plusone(a)