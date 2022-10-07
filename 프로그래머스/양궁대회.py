from itertools import combinations_with_replacement
def solution(n, info):
    answer = []
    cha_value = 0
    arr = [i for i in range(11)]
    for  lion_info in combinations_with_replacement(arr,n):
        print("lion_info",lion_info)
        lion_arr = [0]*11
        lion_cnt , apeach_cnt = 0,0
        for i in lion_info:
            lion_arr[i] += 1

        for i in range(11): #[0 2 2 0 1 0 0 0 0 0 0 0 ]
            if lion_arr[i] > info[i]:
                lion_cnt += 10-i
            elif lion_arr[i] == info[i] == 0:
                continue
            elif lion_arr[i] <= info[i]:
                apeach_cnt += 10-i
        flag = 0
        if lion_cnt > apeach_cnt:
            if cha_value < lion_cnt-apeach_cnt:
                cha_value = lion_cnt-apeach_cnt
                answer = lion_arr

                # 라이언과 어피치의 점수차가 같은 경우일때
                # 가장 낮은 점수를 더 많이 맞힌 경우를 검증하는 로직
            elif cha_value == lion_cnt-apeach_cnt   :
                for i in range(10,-1,-1):
                    if lion_arr[i] == answer[i]==0:
                        continue
                    elif lion_arr[i] > answer[i]:
                        answer = lion_arr
                        break
                    else:
                        break


    if not answer :
        answer.append(-1)
    return answer

n,info = 10,[0,0,0,0,0,0,0,0,3,4,3]

print(solution(n, info))










# from itertools import combinations_with_replacement
# import sys
#
#
# def solution(n, info):
#     answer = []
#     arr = [i for i in range(11)]
#     dic = dict()
#     dic2 = dict()
#     for i in range(11):
#         dic[i] = 10 - i
#         dic2[i] = i
#     max_value = 0
#     cha_value = 0
#     back_score = 0
#
#     for combi in list(combinations_with_replacement(arr, n)):
#         apeach_score = 0
#         lion_score = 0
#         lion_info = [0] * 11
#         for j in combi:
#             lion_info[j] += 1
#
#         #라이언과 어피치 점수 매기기
#         for i in range(11):
#             if lion_info[i] > info[i]:
#                 lion_score += dic[i]
#             elif info[i]>0 and info[i]>=lion_info[i]:
#                 apeach_score += dic[i]
#
#         if lion_info == [3, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0]:
#             print("311,ape, lion", apeach_score,lion_score)
#             print("lion_ino = ", lion_info)
#             print("answer = ",answer)
#             print()
#         elif lion_info == [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 2]:
#             print("111,ape, lion", apeach_score,lion_score)
#             print("lion_ino = ", lion_info)
#             print("answer = ", answer)
#             print()
#
#         if lion_score > apeach_score:
#
#             if lion_score > max_value and abs(apeach_score - lion_score) > cha_value:
#                 max_value = lion_score
#                 cha_value = abs(apeach_score - lion_score)
#                 answer = lion_info
#
#
#             elif lion_score == max_value and abs(apeach_score - lion_score) == cha_value:
#                 for i in range(10,-1,-1):
#                     if lion_info[i]==answer[i]:
#                         continue
#                     elif lion_info[i] > answer[i]:
#                         answer = lion_info
#                     elif lion_info[i] <= answer[i]:
#                         continue
#
#
#
#
#
#
#                 # if res > back_score:
#                 #     cha_value = abs(apeach_score - lion_score)
#                 #     answer = lion_info
#
#     if not answer:
#         answer.append(-1)
#     return answer
#
# print(solution(10,[0,0,0,0,0,0,0,0,3,4,3]))