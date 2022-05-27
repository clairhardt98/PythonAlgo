def solution(S):
    Unique_S=list(set(S))
    cnt_list=[]
    for i in Unique_S:
        cnt=S.count(i)
        cnt_list.append(cnt)

    if cnt_list.count(max(cnt_list))>1:
        print('?')
    else:
        max_index=cnt_list.index(max(cnt_list))
        print(Unique_S[max_index])

S=input().upper()
solution(S)