import sys
N=int(input())

employee=set()
for _ in range(N):
    M=sys.stdin.readline().split()
    if M[1]=='enter':
        employee.add(M[0])
    else:
        employee.discard(M[0])

answer=sorted(employee,reverse=True)

for i in answer:
    print(i)