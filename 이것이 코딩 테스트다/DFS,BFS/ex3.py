N, M = map(int,input().split())

A = []
visited = [[0] * M for _ in range(N)]

cnt = 0
for _ in range(N):
    A.append(list(map(int,input().split())))

def dfs(x,y):
    if x<0 or x>=N or y<0 or y>=M:
        return 0
    else:
        visited[x][y]=1
        dfs(x,y-1)
        dfs(x,y+1)
        dfs(x+1,y)
        dfs(x-1,y)
        return True
    return 0

for i in range(N):
    for j in range(M):
        if dfs(i,j)==True:
            cnt+=1

print(cnt)



