def solution(survey, choices):
    answer = ''
    arr = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']
    num = []
    for i in choices:
        if i == 1 or i == 7:
            num.append(3)
        elif i == 2 or i == 6:
            num.append(2)
        elif i == 3 or i == 5:
            num.append(1)
        else:
            num.append(0)

    dic = dict()

    for i in arr:  # 유형에 따른 0점 dic생성
        dic[i] = 0

    for i in range(len(survey)):
        if choices[i] < 4:
            dic[survey[i][0]] += num[i]
        elif choices[i] > 4:
            dic[survey[i][1]] += num[i]
    # return print(dic)
    if dic['R'] >= dic['T']:
        answer += 'R'
    else:
        answer += 'T'
    if dic['C'] >= dic['F']:
        answer += 'C'
    else:
        answer += 'F'
    if dic['J'] >= dic['M']:
        answer += 'J'
    else:
        answer += 'M'
    if dic['A'] >= dic['N']:
        answer += 'A'
    else:
        answer += 'N'

    return answer