def solution(n, arr1, arr2):
    arr1_map=[None]*n
    arr2_map=[None]*n

    for i in range(0, len(arr1)):
        val=format(arr1[i],'b')
        arr1_map[i]=val.zfill(n)
    for i in range(0, len(arr2)):
        val=format(arr2[i],'b')
        arr2_map[i]=val.zfill(n)
  
    for i in range(0,n):
        arr1_temp=list(arr1_map[i])
        for j in range(0,n):
            if arr1_temp[j]=='0':
                arr1_temp[j]=' '
            else:
                arr1_temp[j]='#'
        arr1_map[i]=list(arr1_temp)

    for i in range(0,n):
        arr2_temp=list(arr2_map[i])
        for j in range(0,n):
            if arr2_temp[j]=='0':
                arr2_temp[j]=' '
            else:
                arr2_temp[j]='#'
        arr2_map[i]=list(arr2_temp)

    for i in range(0,n):
        for j in range(0,n):
            if arr1_map[i][j]==' ' and arr2_map[i][j]==' ':
                arr1_map[i][j]=' '
            else:
                arr1_map[i][j]='#'

    map=[None]*n
    for i in range(n):
        b = ''.join(arr1_map[i])
        map[i]=b

    return map
n=5
arr1=[9, 20, 28, 18, 11]
arr2=[30, 1, 21, 17, 28]

solution(n,arr1,arr2)
