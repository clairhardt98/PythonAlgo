def solution(arr1, arr2):
    answer=[]
    row=len(arr1)
    col=len(arr1[0])
    for i in range(0,row):
        answer.append([])
        for j in range(0,col):
            answer[i].append(arr1[i][j]+arr2[i][j])

    return answer

arr1=[[1],[2]]
arr2=[[3],[4]]
print(solution(arr1,arr2))