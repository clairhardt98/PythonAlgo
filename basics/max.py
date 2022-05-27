from typing import Any, Sequence
def max_of(a: Sequence) -> Any:
    maximum=a[0]
    for i in range(1,len(a)):
        if a[i]>maximum:
            maximum=a[i]
    return maximum

if __name__ == '__main__':
    num=int(input('input num of array:'))
    array=[None]*num

    for i in range(num):
        array[i]=int(input(f'input data of array[{i}]:'))

    print(f'maximum of array is {max_of(array)}')