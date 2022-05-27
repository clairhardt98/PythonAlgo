N,M,K=map(int,input().split())

arr=list(map(int,input().split()))
arr.sort()
temp=[]

sum=0
cnt=0

for _ in range(2):
    temp.append(arr[-1])
    arr.pop()

while True:
    for _ in range(K):
        if M==0:break
        sum+=temp[0]
        M-=1
    if M==0:break
    sum+=temp[1]
    M-=1


print(sum)