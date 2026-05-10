#Brute Force approach to find the number of subarrays that sum up to k
def subarray_sum_k(arr, k):
    count = 0
    for i in range(len(arr)):
        total = 0
        for j in range(i, len(arr)):
            total += arr[j]
            if total == k:
                count += 1
    return count


arr = [1, 1, 1]
k = 2
print(subarray_sum_k(arr, k))

#Optimal approach using Hash Map to find the number of subarrays that sum up to k

def subarray_sum_k_optimal(arr,k):
    count=0
    total=0
    hash_map={0:1}
    for i in range(len(arr)):
        total+=arr[i]
        if total-k in hash_map:
            count+=hash_map[total-k]
        hash_map[total]=hash_map.get(total, 0) + 1
    return count
print(subarray_sum_k_optimal(arr,k))
