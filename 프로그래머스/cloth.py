def solution(n, lost, reserve):
    cloth=[1]*(n+1)
    for i in range(len(reserve)):
        cloth[reserve[i]]+=1
    for i in range(len(lost)):
        cloth[lost[i]]-=1
    for i in range(1,n+1):
        if i!=n:
            if (cloth[i]==0)and(cloth[i-1]==2):
                cloth[i]+=1
                cloth[i-1]-=1
            elif(cloth[i]==0)and(cloth[i+1]==2):
                cloth[i]+=1
                cloth[i+1]-=1
    student=0
    for i in range(1,n+1):
        if cloth[i]!=0:student+=1
    return student

    

n=5
lost=[2, 4]
reserve=[1,3,5]

solution(n,lost,reserve)