import sys
sys.setrecursionlimit(1000000)

N, M = map(int, input().split())
r,c,d= map(int, input().split())


room =[list(map(int, input().split())) for _ in range(N)]
cnt=0
cleared=0
end=False

def clear(r,c):
    global cleared
    room[r][c]=-1
    cleared+=1

def move(r,c,d):
    if d==0:
        return r-1,c
    elif d==1:
        return r,c+1
    elif d==2:
        return r+1,c
    else:
        return r,c-1

def rotation(d):
    if d==0:
        d=3
    else:
        d-=1
    return d

def back(d):
    if d==0:
        d=2
    elif d==1:
        d=3
    elif d==2:
        d=0
    else:
        d=1
    return d

def check(r,c,d,cnt):
    global end
    if end:
        return
    global room
    if room[r][c]==0:
        clear(r,c)#현재 위치가 비어있으면 청소
    
    d_next=rotation(d)#바라보는 방향의 왼쪽 방향을 d_next로 지정
    r_next, c_next=move(r,c,d_next)#왼쪽 방향의 칸의 idx
    if room[r_next][c_next]!=0:#청소가능이 아니라면
        cnt+=1#cnt 1증가시키고
        if cnt==5:#4방향이 전부 청소됐거나 or 벽, 1바퀴 돈 상황
            d_rear=back(d)#바라보는 방향의 반대방향
            r_next, c_next=move(r,c,d_rear)#반대방향의 idx
            if room[r_next][c_next]==1:#반대방향의 idx의 값이 벽일경우
                end=True
            else:#벽이 아닐경우
                cnt=0#cnt초기화
                check(r_next,c_next,d,cnt)#방향 유지한채로 1칸 후진
        check(r,c,d_next,cnt)#다음 방향에서 다시 check
    else:#다음칸이 청소가능
        cnt=0#cnt초기화
        check(r_next,c_next,d_next,cnt)#이동
    


check(r,c,d,cnt)
print(cleared)

