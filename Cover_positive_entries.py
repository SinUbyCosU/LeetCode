def cover_positive_entries(A):
    count=0
    i=0
    n=len(A)

    while i<n:
        if A[i]>0:
            i+=1
        else:
            count+=1
            current_sum=A[i]
            j=i+1
            while j<n and (current_sum+A[j]>0):
                current_sum+=A[j]
                j+=1
            i=j
    return count