def solution(N, stages):
    length = len(stages)    #8
    answer = []
    stagedA=[0]*(N+1)
    stagedB=[0]*(N+1)
    newArr=[]
    for i in range(length):
        stagedA[stages[i]-1] += 1
    stagedB[-1]=stagedA[-1]

    for i in range(N-1,-1,-1):
        stagedB[i] = stagedB[i+1] + stagedA[i]#N-1,i+1조심
    res = 1
    for i in stagedB:
        if i:
            res*=i
    ans = []
    for i in range(N):
        x=0
        if stagedB[i]:
            x = (res//stagedB[i])*stagedA[i]
        else:
            x=0
        ans.append(x)
    dic = dict()
    for i in range(N):
        dic[i+1] = ans[i]
    #print("stagedA",stagedA)
    #print("stagedB",stagedB)
    #print(dic)
    new_dic = sorted(dic.items(),key=lambda x:x[1], reverse=True )
    #print(new_dic)
    for i in new_dic:
        answer.append(i[0])

    return answer