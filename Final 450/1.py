def reverseArr_naive(arr):
    reversed = []
    for i in range(len(arr)-1, -1, -1):
        reversed.append(arr[i])
    return reversed
    
def reverseArr(arr):
    start = 0
    end = len(arr)-1
    
    while start<end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr
    
print(reverseArr([1,2,3,4]))