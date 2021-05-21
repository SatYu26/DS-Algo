def minN(arr):
    mx = float('-inf')
    mi = float('inf')
    for i in range(len(arr)):
        if arr[i] >= mx:
            mx = arr[i]
        if arr[i] <= mi:
            mi = arr[i]
    return mx, mi
            
        
    
print(minN([1,2,3,4]))