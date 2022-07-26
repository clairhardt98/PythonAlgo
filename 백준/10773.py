n=int(input())

m=[]
for _ in range(n):
    k=int(input())
    if k==0:
        m.pop()
    else:
        m.append(k)

print(sum(m))