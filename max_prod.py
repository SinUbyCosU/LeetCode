def max_prod(nums):
    global_max=nums[0]
    suffix=0
    prefix=0
    n=len(nums)
    for i in range(n):
        prefix=(prefix or 1)*nums[i]
        suffix=(suffix or 1)*nums[n-i-1]
        global_max=max(global_max,suffix,prefix)
    return global_max