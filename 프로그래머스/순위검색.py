from bisect import bisect_left
from collections import defaultdict
from itertools import combinations
def solution(info, query):
    answer = []
    dic = defaultdict(list)

    for inf in info:    #공백으로 구분되어 있어
        inf = inf.split(' ')
        info_key = inf[0:-1]
        info_value = int(inf[-1])
        for i in range(5):#안뽑는 경우부터 4개 전부를 뽑는 경우까지 (점수빼고)
            combi = list(combinations(info_key,i))
            for j in combi:
                res = ''.join(j)
                dic[res].append(info_value)
    #O(N)
    for key in dic:
        dic[key].sort()

    ##== query길이 10만 , 쿼리 갯수만큼 ==##

    for q in query: #마지막 음식과 점수는 and가 아니라 공백으로 구분되어 있어
        q = q.split(' ')
        print("q",q)
        q_key = q[:-1]
        q_value = int(q[-1])

        ##==O(3*7)==##
        for i in range(3):
            q_key.remove('and') #한번 삭제할때마다 O(N) 앞에있는 것부터 한번에 하나씪 삭제하게됨
        ##==O(4*4)==##
        while '-' in q_key:
            q_key.remove('-')

        query_key = ''.join(q_key)
        print("q_key",q_key)
        ##==dic길이 : 54 // info의 경우의수==##
        if query_key in dic:
            scoreList = dic[query_key]

        ##==이분탐색 log(N)==##
            if len(scoreList) > 0:
                answer.append(len(scoreList) - bisect_left(scoreList,q_value))
                # left, right = 0, len(scoreList)
                # while left < right:
                #     mid = (left + right) // 2
                #     if scoreList[mid] >= q_value:
                #         right = mid
                #     else:
                #         left = mid + 1
                # answer.append(len(scoreList) - left)
        else:
            answer.append(0)
    print("answer",answer)

    return answer


info =["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
solution(info,query)
