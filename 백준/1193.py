x=int(input())
lr=1
n=0

cnt=0
while True:
    for i in range(n):
        if(lr==1):
            cnt+=1
            if(cnt==x):
                print(i+1 ,"/",n-i,sep='')
                break
            
        else:
            cnt+=1
            if(cnt==x):
                print(n-i, "/", i+1,sep='')
                break
    n+=1
    if (lr==1):lr=0
    else:lr=1
    if(cnt==x):break


