def MajorityElement2(nums):
    if not nums:
            return[]
        cad1,cad2=None,None
        count1,count2=0,0
        for num in nums:
            if num==cad1:
                count1+=1
            elif num==cad2:
                count2+=1
            elif count1==0:
                cad1=num
                count1+=1
            elif count2==0:
                cad2=num
                count2+=1
            else:
                count1-=1
                count2-=1
        result=[]
        threshold=len(nums)//3
        for cad in [cad1,cad2]:
            if cad is not None and nums.count(cad)>threshold:
                result.append(cad)
        return result

        
