#Brute Force
def brute_2_sum(arr, tar):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i]+arr[j] == tar:
                return [i,j]

print(brute_2_sum([2,7,11,15], 9))