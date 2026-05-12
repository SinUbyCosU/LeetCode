def Missing_Number(nums):
    n=len(nums)
    exp_sum=sum(nums)
    act_sum=n*(n+1)//2
    return act_sum-exp_sum