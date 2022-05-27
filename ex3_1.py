N=int(input())

coin_type=[500,100,50,10]
cnt=0
for coin in coin_type:
    cnt+=N//coin
    N=N-coin*(N//coin)

print(cnt)