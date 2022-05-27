def solution(N, stages):
    clear=[0]*N
    fail=[0]*N
    failure_rate=[0]*N

    for i in range (0,N):
        clear[i]=len(list(filter(lambda x:x>i+1,stages)))
        fail[i]=len(list(filter(lambda x:x==i+1,stages)))

    for i in range(0,N):
        if fail[i]+clear[i]==0:
            failure_rate[i]=0
        else:
            failure_rate[i]=float(fail[i]/(fail[i]+clear[i]))
    
    temp=[0]*N
    for i in range (N):
        temp[i]=[failure_rate[i],i,1]
    

    failure_rate.sort(reverse=True)
    answer=[0]*N

    for i in range(0,N):
        for j in range(0,N):
            if failure_rate[i]==temp[j][0] and temp[j][2]==1:
                answer[i]=temp[j][1]+1
                temp[j][2]=0
                break
        

    return answer

stages=[2, 1, 2, 6, 2, 4, 3, 3]
N=5
print(solution(N,stages))

