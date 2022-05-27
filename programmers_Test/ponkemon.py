def solution(nums):
    temp=len(nums)//2
    count=0
    for i in range(0,len(nums)):
        if nums[i]!=0:
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:nums[j]=0
    for i in range(len(nums)):
        if nums[i]!=0:count+=1
    
    if count>temp:answer=temp
    else :answer=count
    return answer

nums=[3,3,3,2,2,4]
print(solution(nums))