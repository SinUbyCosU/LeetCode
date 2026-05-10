#Brute Force
def brute_2_sum(arr, tar):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i]+arr[j] == tar:
                return [i,j]

print(brute_2_sum([2,7,11,15], 9))

#better approach(not optimal O(nlogn))

def better_2_Sum(arr, tar):
    sorted_arr=sorted(arr, reverse=True)
    left=0
    right=len(arr)-1
    while left<right:
        if sorted_arr[left]+sorted_arr[right] == tar:
            return [arr.index(sorted_arr[left]), arr.index(sorted_arr[right])]
        elif sorted_arr[left]+sorted_arr[right] >tar:
            right-=1
        else:
            left+=1
        
print(better_2_Sum([2,7,11,15], 9))