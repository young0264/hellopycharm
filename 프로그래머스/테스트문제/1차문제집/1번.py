def solution(X, Y):
    answer = ''
    dic = dict()
    flag = 0
    flag2 = 0
    for i in X:
        if i not in dic:
            dic[i] = [1,0]
        else:
            dic[i][0] += 1
    for i in Y:
        if i in dic:
            flag = 1
            dic[i][1] += 1

    if not flag:
        return "-1"
    print("dic",dic)
    for i in dic:
        x = min(dic[i])
        answer += i*x
        print("flag2",flag2)
        if i != '0' and x != 0:
            flag2 = 1
    if not flag2:
        return "0"

    answer = ''.join(sorted(answer,reverse=True))

    return str(answer)