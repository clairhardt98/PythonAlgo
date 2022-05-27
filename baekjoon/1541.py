S=input().split('-')
print(int(S))

answer=[]
for i in S:
    tmp=0
    n=i.split('+')
    for j in n:
        tmp+=int(j)
    answer.append(tmp)