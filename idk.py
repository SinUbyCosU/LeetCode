def positive(num):
    count=0
    i=0
    n=len(num)
    while i<n:
        if num[i]>=0:
            i=i+1
        else:
            count+=1
            current_sum=num[i]
            j=i+1
            while j<n and (current_sum+num[j]>0):
                current_sum+=num[j]
                j+=1
            i=j
        return count
        