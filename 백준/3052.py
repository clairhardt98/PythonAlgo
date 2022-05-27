S=set()
for _ in range(10):
    A=int(input())
    S.add(A%42)

print(len(S))