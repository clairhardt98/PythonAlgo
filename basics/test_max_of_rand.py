import random
from max import max_of

num=int(input('input number of random numbers :'))
lo=int(input('input minimum of random numbers :'))
hi=int(input('input maximum of random numbers :'))

x=[None]*num

for i in range(num):
    x[i]=random.randint(lo,hi)

print('array of random number is')
print(x)
print(f'maxinum of x is {max_of(x)}')