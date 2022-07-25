#시뮬레이션 유형

n = int(input())

x, y = 1, 1 #시작점

plans = input().split()

dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']
#x, y축의 이동

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            #이동 방향에 따라서 nx와 ny를 결정
    if nx<1 or ny<1 or nx>n or ny>n :
        continue
    #조건이 만족하지 않는다면 continue
    x, y = nx, ny

print(x, y)