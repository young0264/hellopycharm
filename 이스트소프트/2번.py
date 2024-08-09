def solution(queue):

    answer = []
    len_q = len(queue)
    dic = dict()

    # init_dictionary
    for i in range(1,4):
        dic[i] = 0

    # queue 원소, dictionary에 key값 count
    for q in queue:
        dic[q] = dic.get(q, 0) + 1

    # 여유공간 갯수 count(최댓값과의 차이의 합)
    def getDiffOfNum(new_dic):
        max_val = max(new_dic.values())
        num_diff = 0

        for d in new_dic:
            num_diff += (max_val - new_dic[d])

        return num_diff

    # 여유공간이 같을 때
    # 추가해야하는 숫자 count -> array return
    def getNumForAdd(new_dic):
        max_val = max(new_dic.values())
        arr = []

        for i in range(1,4):
            arr.append(max_val-new_dic[i])

        return arr


    for i in range(len_q):
        # 현재 진행중인 여유공간 n번째와 여유공간의 갯수가 같으면 break
        if i == getDiffOfNum(dic):
            answer = getNumForAdd(dic)
            break

        dic[queue[i]] -= 1

    return answer