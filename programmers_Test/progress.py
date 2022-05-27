def solution(progresses,speeds):
    answer=[]
    day=1
    count=0
    while len(progresses)>0:
        if progresses[0]+speeds[0]*day>=100:
            del progresses[0]
            del speeds[0]
            count+=1
        else:
            if count:
                answer.append(count)
            day+=1
            count=0
        
    answer.append(count)
        
    return answer
progresses=[93, 30, 55]
speeds=[1, 30, 5]

print(solution(progresses,speeds))
        