from itertools import permutations
def solution(user_id, banned_id):
    answer = 0
    length = len(banned_id)
    ans_arr = []
    for permu in permutations(user_id,length):
        permu = list(permu)
        visited = [0]*length
        # print("permu",permu)
        flag = 0
        for i in range(length): #banned_id
            if len(banned_id[i]) == len(permu[i]):
                # print((banned_id[i]),(permu[i]))
                for j in range(len(banned_id[i])):
                    if banned_id[i][j] !='*' and banned_id[i][j] != permu[i][j]:
                        flag = 1
            else:   #길이가 같지 않아서 조건 성립이 안될때
                flag = 1
                break
        if not flag :
            res = ''
            # ans_arr.append(sorted(permu))
            for i in sorted(permu):
                res+=i
            ans_arr.append(res)
            # print("permu",sorted(permu))
            # answer +=1

    # print(answer)
    # print("ansarr",ans_arr)
    # print(len(list(set(ans_arr))))
    return answer

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "abc1**"]

solution(user_id, banned_id)

# def solution(user_id, banned_id):
#     answer = 0
#
#     for ban_id in banned_id:
#         ban_id = list(ban_id)
#         result = 0
#         for i in range(len(ban_id)):
#             flag = 0
#             for u_id in user_id:
#                 u_id = list(u_id)
#                 if len(ban_id) == len(u_id) and ( ban_id[i] =='*' or ban_id[i]==u_id[i]):
#                     print(ban_id,u_id,user_id)
#                     continue
#
#                 else:
#                     flag = 1
#             if not flag:
#                 result += 1
#             print()
#         print("res",result)
#         print()
#
#
#
#
#
#
#
#     return answer
#
#
# user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
# banned_id = ["fr*d*", "abc1**"]
# solution(user_id,banned_id)