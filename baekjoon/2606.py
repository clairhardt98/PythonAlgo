from collections import deque
import sys
read=sys.stdin.readline

def bfs(v):
    q=deque()
    q.append(v)
    visited[v]=1
    while q:
        v=q.popleft()
        for i in range(1,n+1):
            if visited[i]==0 and com[v][i]==1:
                q.append(i)
                visited[i]=1


n=int(read())
m=int(read())

com=[[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b=map(int, read().split())
    com[a][b]=com[b][a]=1
visited=[0]*(n+1)


bfs(1)
answer=visited.count(1)
print(answer-1)



