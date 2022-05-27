counter =0
ptr=0
prime=[None]*500

prime[ptr]=2

ptr+=1

x=int(input('x까지 소수를 출력합니다. x : '))
for n in range (3,x,2):
    for i in range(1,ptr):
        counter+=1
        if n%prime[i]==0:
            break

    else:
        prime[ptr]=n
        ptr+=1
for i in range(ptr):
    print(prime[i])
