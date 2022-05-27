N,M=map(int,input().split())

answer=0
for _ in range(N):
    cards=list(map(int,input().split()))
    if answer<min(cards):
        answer=min(cards)

print(answer)

