def solution(lottos, win_nums):
    count=0
    unknown=0
    for i in range(0,6):
        if lottos[i]==0:
            unknown+=1
            continue
        for j in range(0,6):
            if lottos[i]==win_nums[j]:count+=1

   
    answer = [get_rank(count+unknown),get_rank(count)]
    return answer

def get_rank(count):
    rank=7-count
    if rank>5:rank=6
    return rank