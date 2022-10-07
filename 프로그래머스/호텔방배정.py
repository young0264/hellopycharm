
import sys
sys.setrecursionlimit(10**5)
def find(num,dic):
    if num not in dic:
        dic[num] = num+1
        return num
    number = find(dic[num],dic)
    dic[num] = number +1
    return number


def solution(k, room_number):
    answer = []
    dic = dict()
    for num in room_number:
        res = find(num,dic)
        answer.append(res)
    return answer


# k = 10
# room_number = [1, 3, 4, 1, 3, 1]
# solution(k, room_number)


# k = 10
# room_number = [1, 3, 4, 1, 3, 1]
# solution(k, room_number)
#시간초과코드
def solution(k, room_number):
    answer = []
    dic = dict()

    for num in room_number:
        while True:
            if num in dic:
                num = num+1
            else:
                answer.append(num)
                dic[num] = num + 1
                break
    print("ans",answer)
    return answer
k = 10
room_number = [1, 3, 4, 1, 3, 1]
solution(k, room_number)

