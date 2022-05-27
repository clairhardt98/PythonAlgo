def wifi(distance):
    cnt=1
    cur_X=X[0]
    for i in range(1,len(X)):
        if X[i]>=cur_X+distance:
            cnt+=1
            cur_X=X[i]
    return cnt

N,C=map(int,input().split())
X=[]
for _ in range(N):
    X.append(int(input()))

X.sort()

result=0
srt=1
end=max(X)-min(X)

while srt<=end:
    mid=(srt+end)//2
    if wifi(mid)>=C:
        result=mid
        srt=mid+1
    else:
        end=mid-1

print(result)


