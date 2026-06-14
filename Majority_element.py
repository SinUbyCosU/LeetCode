def Majority_element(nums):
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    return candidate
    #test
print(Majority_element([2,2,1,1,1,2,2]))


#Revison Round
