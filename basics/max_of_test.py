from max import max_of

number=0
x=[]

while True:
    s=input('input data. if you put "end", stop getting data. :')
    if s=='end':
        break
    x.append(int(s))
    number += 1

print(f'you entered {number} data.')
print(f'maximum of your data is {max_of(x)}')