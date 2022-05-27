K,N=map(int,input().split())
LAN=[]
for i in range(K):
    LAN.append(int(input()))

srt=1
end=max(LAN)
LAN.sort()
result=0

while srt<=end:
    Length=0
    mid=(srt+end)//2
    
    for i in LAN:
        Length+=(i//mid)

    if Length>=N:
        result=mid
        srt=mid+1
    elif Length<N:
        end=mid-1

print(result)

