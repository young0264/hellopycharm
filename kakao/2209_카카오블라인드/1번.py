#일로 환산
def change_day(s):
    year, month, day = s.split('.')
    res = int(year)*12*28 + int(month)*28 + int(day)
    return res

def change_Pday(s):
    global dic
    year, month, days = s.split('.')
    days = days.split(' ')
    day, day_type = days[0], days[1]
    res = int(year)*12*28 + int(month)*28 + int(day) + dic[day_type]*28
    return res

def solution(today, terms, privacies):
    global dic
    answer = []
    now = change_day(today)
    dic = dict()

    for i in terms:
        t,v = i.split(' ')
        dic[t] = int(v)

    for i in range(len(privacies)):
        if now >= change_Pday(privacies[i]):
            answer.append(i+1)

    return answer