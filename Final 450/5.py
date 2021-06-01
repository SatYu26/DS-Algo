# method 1

def arrange(A):
    n = len(A)
    negative = []
    positive = []
    
    for i in range(n):
        if A[i] < 0:
            negative.append(A[i])
        if A[i] >= 0:
            positive.append(A[i])
    return negative + positive

# method 2

def shiftall(arr,left,right):
   
    while left<=right:
      
        if arr[left] < 0 and arr[right] < 0:
          left+=1
           
        elif arr[left]>0 and arr[right]<0:
          arr[left], arr[right] = arr[right],arr[left]
          left+=1
          right-=1
    
        elif arr[left]>0 and arr[right]>0:
          right-=1
          
        else:
          left+=1
          right-=1
    return arr
    
    
arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
    
print(arrange(arr))