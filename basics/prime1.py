counter=0

x=int(input('x까지 소수를 출력합니다. x : '))
for n in range(2,x):
    for i in range(2,n):
        counter +=1
        if n%i==0:
            break

    else:
        print(n)