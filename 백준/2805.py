N,M=map(int,input().split())

Tree=[None]*N

Tree=list(map(int,input().split()))
srt=0
end=max(Tree)
result = 0
while srt<=end:
    mid=(srt+end)//2
    wood=0
    for i in Tree:
        if i-mid>=0:
            wood+=i-mid#tree를 탐색해서 H위의 나무를 자름

    if wood>=M:
        result = mid
        srt=mid+1

    elif wood<M:
        end=mid-1

print(result)