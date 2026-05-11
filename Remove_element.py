#remove element
def removeElement(nums,val):
    i=0
    for val in range(len(nums)):
        if val!=nums[i]:
            nums[i]=nums[val]
            i+=1
        return i