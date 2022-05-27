def solution(array, commands):
    answer=[]
    for i in commands:
        array_temp=[]
        for j in range(i[0]-1,i[1]):
            array_temp.append(array[j])
        array_temp.sort()
        answer.append(array_temp[i[2]-1])
    return answer

array_input=[1, 5, 2, 6, 3, 7, 4]
commands_input=[[2, 5, 3], [4, 4, 1], [1, 7, 3]]


print(f'{solution(array_input,commands_input)}')