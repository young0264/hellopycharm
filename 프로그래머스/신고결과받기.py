def solution(id_list, report, k):
    report = list(set(report))
    answer = []
    dic = dict()
    bad_users_arr = []
    answer_dic = dict()
    for v in report:
        report_user, bad_user = v.split()
        dic[bad_user] = dic.get(bad_user, 0) + 1  # dic
        answer_dic[report_user] = answer_dic.get(report_user, []) + [bad_user]

    for key in dic:
        if dic[key] >= k:
            bad_users_arr.append(key)

    for key in id_list:
        cnt = 0
        if key not in answer_dic:
            answer.append(0)
            continue
        for v in answer_dic[key]:
            if v in bad_users_arr:
                cnt += 1
        answer.append(cnt)

    return answer