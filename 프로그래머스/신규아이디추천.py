from collections import deque


def solution(new_id):
    answer = ''
    answer1 = ''
    answer2 = ''
    answer3 = ''
    new_id = list(new_id)
    # 첫번째조건 대문자 -> 소문자
    for i in range(len(new_id)):
        x = ord(new_id[i])
        if 65 <= x <= 90:
            answer += chr(x + 32)
        elif x == 45 or x == 46 or x == 95 or 97 <= x <= 122:
            answer += new_id[i]

        elif 48 <= x <= 57:
            answer += new_id[i]

    answer = list(answer)
    flag = 0
    for i in range(len(answer)):
        if answer[i] == '.':
            if flag:
                continue
            else:
                answer1 += answer[i]
                flag = 1
        else:
            answer1 += answer[i]
            flag = 0

    if len(answer1) > 2 and answer[0] == '.' and answer[-1] == '.':
        answer1 = answer1[1:-1]
    elif answer[0] == '.':
        answer1 = answer1[1:]
    elif answer[-1] == '.':
        answer1 = answer1[:-1]
    elif len(answer1) == 1 and answer1[0] == '.':
        answer1 = ''

    print("answer1", answer1)

    if len(answer1) == 0:
        answer1 = 'a'

    if len(answer1) >= 16:
        for i in range(16):
            answer2 = answer1[:15]

    elif len(answer1) <= 2:
        answer2 += answer1
        for i in range(3 - len(answer1)):
            answer2 += answer1[-1]
    else:
        answer2 = answer1

    if len(answer2) > 2 and answer2[-1] == '.':
        answer2 = answer2[:-1]

    print("answer2", answer2)
    return answer2