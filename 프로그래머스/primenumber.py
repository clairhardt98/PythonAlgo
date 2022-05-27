def solution(nums):
    count=0
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                sum=nums[i]+nums[j]+nums[k]
                if sum%2==1:
                    l=3
                    while sum%l!=0:
                        l+=1
                        if sum==l:count+=1
    return count