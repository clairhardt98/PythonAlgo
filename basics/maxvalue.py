def max3(a,b,c):
    maximum=a
    if b>maximum:maximum=b
    if c>maximum:maximum=c
    return maximum

a=int(input('정수 a의 값을 입력하세요:'))
b=int(input('정수 b의 값을 입력하세요:'))
c=int(input('정수 c의 값을 입력하세요:'))

M=max(a,b,c)
print(f'최댓값은 {M}입니다.')