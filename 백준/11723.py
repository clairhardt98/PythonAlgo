import sys
S=set()
M=int(input())
for _ in range(M):
    N=sys.stdin.readline().strip().split()

    if len(N)==1:
        A=N[0]
    else:
        A,B=N[0],N[1]
        B=int(B)

    if A=='add':
        S.add(B)

    elif A=='remove':
        S.discard(B)

    elif A=='check':
        print(1 if B in S else 0)

    elif A=='toggle':
        if B in S:
            S.discard(B)
        else:
            S.add(B)

    elif A=='all':
        S=set([i for i in range(1,21)])
    else:
        S=set()

