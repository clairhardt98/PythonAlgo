def solution(s):
    z=[]
    cnt=1
    min_length=len(s)
    for i in range(1,len(s)//2+1):
        tmp=s[0:i]  #비교할 문자열 지정
        cnt=1
        a=''    #압축된 문자열
        for j in range(i,len(s),i):
            if tmp==s[j:j+i]: #j 늘려가며 문자열 비교
                cnt+=1        #같으면 cnt++
            else:   #비교 종료
                if cnt>1:    #같은게 2개 이상 있었으면
                    a=a+str(cnt)+tmp    #문자열압축
                else:
                    a=a+tmp     #아니라면 그냥 입력
                tmp=s[j:j+i]    #비교 종료시 같지 않았던 문자열 슬라이스를 tmp로지정
                cnt=1           #cnt 초기화
        if cnt>1:
            a=a+str(cnt)+tmp
        else:
            a=a+tmp
         
        if len(a)<min_length:
            min_length=len(a)
    
    return min_length

s="aabbaccc"
print(solution(s))