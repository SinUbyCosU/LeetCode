#Brute Force
def productExceptSelfBruteForce(nums):
    result=[]
    n=len(nums)
    for i in range(n):
        product=1
        for j in range(n):
            if i!=j:
                product*=nums[j]
                result.append(product)
            return result

#Optimal Solution
def opt(nums):
    n=len(nums)
    result=[1]*n
    prefix=1
    for i in range(n):
        result[i]=prefix
        prefix*=nums[i]
    suffix=1
    for i in range(n-1,-1,-1):
        result[i]*=suffix
        suffix*=nums[i] 
    return result