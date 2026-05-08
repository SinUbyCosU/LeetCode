#Maximum subarray sum

def max_subarray_sum(arr):
    max_Sum=float('-inf')
    current_sum=0
    for i in range(len(arr)):
        current_sum= max(current_sum+arr[i], arr[i])
        max_Sum=max(max_Sum,current_sum)
    return max_Sum

arr=[-2,1,-3,4,-1,2,1,-5,4]
print(max_subarray_sum(arr))
