n, m = map(int, input().split())

vmap = [[0] * m for _ in range(n)]#2차원 배열로 방문 맵 생성

x, y, d = map(int, input().split())

vmap[x][y] = 1 # 현재 위치 방문 처리

Map = []
for i in range(n):
    Map.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
#방향 지정

def turn():
    global d
    d=d-1
    if d<0:d=3

cnt=0
turn_cnt = 0
while True:
    turn()
    turn_cnt+=1
    next_x = x+dx[d]
    next_y = y+dy[d]
    if vmap[next_x][next_y] == 0 and Map[next_x][next_y] == 0:
        x=next_x
        y=next_y
        vmap[x][y]=1
        turn_cnt = 0
    
    if turn_cnt == 4:
        back_x = x-dx[d]
        back_y = x-dy[d]
        if Map[back_x][back_y] == 0:
            x=back_x
            y=back_y
            turn_cnt=0
        else:
            break

for i in range(n):
    for j in range(m):
        if vmap[i][j]==1:cnt+=1


print(cnt)

