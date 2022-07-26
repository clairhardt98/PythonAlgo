answer = []

t=int(input())
for _ in range(t):
    H, W, N = map(int, input().split())

    cnt=0
    fr=0
    ed=0

    for i in range(W):
        if cnt==N : break

        if ed==W:ed=1
        else:ed+=1

        for j in range(H):
            if fr==H:
                fr=1
                cnt+=1
                if cnt==N : break
            else:
                fr+=1
                cnt+=1
                if cnt==N : break


    if(ed<10):
        m=str(fr)+"0"+str(ed)
    else:
        m=str(fr)+str(ed)
    answer.append(m)
for i in range(t):
    print(int(answer[i]))


