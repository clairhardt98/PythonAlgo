n=int(input('출력할 개수:'))
w=int(input('몇 개마다 줄바꿈?:'))

for _ in range(n//w):
    print('*' * w)

rest=n%w
print('*'*rest)


