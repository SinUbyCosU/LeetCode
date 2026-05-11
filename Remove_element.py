#remove element
def removeElement(nums,val):
    i=0
    for j in range(len(nums)):
        if nums[j]!=val:
            nums[i]=nums[j]
            i+=1
    return i

#test

print(removeElement([3,2,2,3], 3))