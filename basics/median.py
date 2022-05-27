def med3(a,b,c):
    if  a>=b:
        if  b>=c:
            return b
        elif    a<=c:
            return a
        else:
            return c
    elif    a>c:
        return a
    elif    b>c:
        return c
    else:
        return b

a=int(input('정수 a의 값을 입력하세요:'))
b=int(input('정수 b의 값을 입력하세요:'))
c=int(input('정수 c의 값을 입력하세요:'))

median_Value=med3(a,b,c)
print(f'세 정수의 중간 값은 {median_Value}입니다.')