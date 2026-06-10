random.shuffle(nums)
target_index=len(nums)-k
def findkthLargetst(A, target):
    if len(A)==0:
        return A[0]
    pivot=A[len(A)//2]

    left=[x for x in A if x>pivot]
    mid=[x for x in A if x==pivot]
    right=[x for x in A if x<pivot]

    if target<len(left):
        return findkthLargetst(left, target)
    elif target<len(left)+len(mid):
        return pivot
    else:
        new_target=target-len(left)-len(mid)
        return findkthLargetst(right, new_target)
    return findkthLargest(nums, target_index)
    M#