import math

def solution(str):
    dartResult=list(str)
    print(dartResult)
    total_score=0
    scoreboard=[0]*3
    bonused=[0]*3
    game=0

    for i in range(1,len(dartResult)):
        cur=dartResult[i]
        
        if cur=='S' or cur=='D' or cur=='T':
            if i>1:game+=1
            scoreboard[game]=option(dartResult[i-1],cur)
        
        if cur=='*' or cur=='#':
            if cur=='*' and game==0:
                scoreboard[game]=bonus(scoreboard[game],cur)
                bonused[game]=1
            elif cur=='*' and game>0:
                scoreboard[game]=bonus(scoreboard[game],cur)
                scoreboard[game-1]=bonus(scoreboard[game-1],cur)
                if bonused[game-1]==1:
                    scoreboard[game-1]=bonus(scoreboard[game-1],cur)
                bonused[game]=1
            else:
                scoreboard[game]=bonus(scoreboard[game],cur)
                bonused[game]=1
           
    for i in range(len(scoreboard)):
        total_score+=int(scoreboard[i])
    
    return total_score


def option(data,char):
    score=0
    if char=='D':
        score=int(data)*int(data)
    elif char=='T':
        score=int(data)*int(data)*int(data)
    elif char=='S':
        score=data
    return score

def bonus(score,char):
    if char=='*':
        score*=2
    elif char=='#':
        score*=-1
    return score

data='1S2D*3T'
print(solution(data))