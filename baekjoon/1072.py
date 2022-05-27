
def solution(X,Y):
    Z_temp=Y*100//X
    S=0
    E=1000000000
    result=0
    while S<=E:
        M=(S+E)//2
        Z=(Y+M)*100//(X+M)
        if Z>Z_temp:
            E=M-1
            result=M
        else:
            S=M+1
        
    print(result if result!=0 else -1)

X,Y=map(int,input().split())
solution(X,Y)