import sys
read=sys.stdin.readline

n=int(read())
house=[[0]*n for _ in range(n)]
visited=[[0]*n for _ in range(n)]

temp=[None]*n
for i in range(n):
    temp[i]=input()
    for j in range(n):
        s=int(temp[i][j])
        house[i][j]=s

dx=[-1,1,0,0]
dy=[0,0,1,-1]


def dfs(x,y,z):
    global num
    visited[x][y]=1
    if house[x][y]==1:
        num+=1
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<n:
            if visited[nx][ny]==0 and house[nx][ny]==1:
                dfs(nx,ny,z)

cnt=1
numlist=[]
num=0

for i in range(n):
    for j in range(n):
        if house[i][j]==1 and visited[i][j]==0:
            dfs(i,j,cnt)
            numlist.append(num)
            num=0

print(len(numlist))
numlist.sort()
for i in range(len(numlist)):
    print(numlist[i])


