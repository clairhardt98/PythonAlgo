class USER:
    UID=0
    Name=''
    InOut=False

def solution(record):
    InOut=[]
    Name=[]
    UID=[]
    for char in record:
        j=0
        cnt=0
        for i in range (0,len(char)):
            if char[i]==' ':
                tmp=char[j:i]
                j=i+1
                if tmp=='Enter':
                    InOut.append(tmp)
                else:
                    InOut.append(tmp)
    print(InOut)
    print(UID)
    print(Name)
    answer = []
    
    return answer

record=["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
solution(record)