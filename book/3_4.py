N,K=map(int,input().split())

cnt=N%K

N=N-N%K

while True:
    N=N//K
    cnt+=1
    if N==1:break
    
print(cnt)


