def solution(n):
    answer=[]

    if n==1:
        answer.append('1')
    elif n==2:
        answer.append('2')
    elif n==3:
        answer.append('4')
    else:
        while n>0:
            q,r=divmod(n-1,3)
            if r==2:
                answer.append('4')
            else:
                answer.append(str(r+1))
            n=q
    
    return(''.join(answer[::-1]))
            

solution(1)