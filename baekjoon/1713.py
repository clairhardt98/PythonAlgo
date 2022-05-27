N=int(input())
Rnum=int(input())
Rarr=list(map(int,input().split()))

student=[]
for i in range(Rnum):
    if len(student)<N:
        student.append([Rarr[i],1])
    else:
        Rmax=student[0][1]
        for j in range(1,len(student)):
            if Rmax<student[j][i]:
                Rmax=student[j][i]

        Rmax=max(student[])
        if Rarr[i]
    

print(student)
