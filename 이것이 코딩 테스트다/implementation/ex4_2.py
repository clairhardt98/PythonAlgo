#나이트가 움직이는 경우의 수를 미리 배열로 설정

n = input()

x = int(n[1])
y = int(ord(n[0])) - int(ord('a')) + 1

steps = [(-2,-1),(-2,1),(2,-1),(2,1),(-1,-2),(-1,2),(1,-2),(1,2)]

cnt = 0

for step in steps:
    nx = x + step[0]
    ny = y + step[1]
    if nx<1 or ny<1 or nx > 8 or ny > 8:
        continue
    cnt+=1

print(cnt)