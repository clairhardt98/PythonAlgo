n = int(input())

cnt = 0 #3의 개수
for i in range(n+1):#시
    for j in range(60):#분
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):#string으로 형 변환 하여 한 단어로 합친 후 '3'이 있는지 검사
                cnt+=1

print(cnt)
