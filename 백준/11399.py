N=int(input())
P=list(map(int,input().split()))

P.sort()

answer=[P[0]]
for i in range(1,N):
    answer.append(answer[-1]+P[i])

print(sum(answer))