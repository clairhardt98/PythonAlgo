def solution(answers):
    answer = []
    answer1=man_1(answers)
    answer2=man_2(answers)
    answer3=man_3(answers)
    max_of_answers=max(answer1,answer2,answer3)
    if answer1==max_of_answers:
        answer.append(1)
    if answer2==max_of_answers:
        answer.append(2)
    if answer3==max_of_answers:
        answer.append(3)
    answer.sort()
    return answer

def man_1(answers):
    correct=0
    answers_man_1=[]
    j=1
    for i in range(0,len(answers)):
        answers_man_1.append(j)
        j+=1
        if j==6:j=1
    for i in range(0,len(answers)):
        if answers[i]==answers_man_1[i]:
            correct+=1
    return correct

def man_2(answers):
    correct=0
    answers_man_2=[None]*len(answers)
    j=1
    for i in range (0,len(answers)):
        if i%2==0:
            answers_man_2[i]=2
        else:
            answers_man_2[i]=j
            if j==1:j+=2
            else: j+=1
            if j==6:j=1
    for i in range(0,len(answers)):
        if answers[i]==answers_man_2[i]:
            correct+=1
    return correct

def man_3(answers):
    correct=0
    answers_man_3=[None]*len(answers)
    j=0
    for i in range (0,1+len(answers)//2):
        if j==0:
            answers_man_3[2*i]=3
        elif j==1:
            answers_man_3[2*i]=1
        elif j==2:
            answers_man_3[2*i]=2
        elif j==3:
            answers_man_3[2*i]=4
        elif j==4:
            answers_man_3[2*i]=5
        j+=1
        if j==5:j=0
    for i in range(0,len(answers)):
        if i%2==1:
            answers_man_3[i]=answers_man_3[i-1]
    for i in range (0,len(answers)):
        if answers[i]==answers_man_3[i]:
            correct+=1
    return correct
        