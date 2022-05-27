from bisect import bisect_left,bisect_right

N=int(input())
C=list(map(int,input().split()))
M=int(input())
D=list(map(int,input().split()))

S=[]
C.sort()

for i in D:
    temp=bisect_right(C,i)-bisect_left(C,i)
    S.append(temp)
for i in S:
    print(i,end=' ')

