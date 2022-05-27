N=int(input())
A=list(map(int,input().split()))
M=int(input())
B=list(map(int,input().split()))

A.sort()

for i in B:
    srt=0
    end=len(A)-1

    while True:
        mid=(srt+end)//2
        if A[mid]==i:
            print(1)
            break
        elif A[mid]>i:
            end=mid-1
        elif A[mid]<i:
            srt=mid+1

        if srt>end:
            print(0)
            break




