def solution(n):
    print(2**n-1)
    Hanoi(n,1,2,3)
    
def Hanoi(n,srt,aux,dst):
        if n==1:
            print(srt,dst)
            return 1
    
        return Hanoi(n-1,srt,dst,aux)+Hanoi(1,srt,aux,dst)+Hanoi(n-1,aux,srt,dst)

n=int(input())
solution(n)



