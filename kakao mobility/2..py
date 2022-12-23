def solution(id_list, k):
    answer = 0
#dictionary[elem] = dictioanry.get(elem,0)+1
    dic = dict()

    for ids in id_list:
        id = ids.split(' ')
        s = set(id)
        for i in s:
            if i not in dic:
                dic[i] = 1
                answer += 1
            elif dic[i] < k :
                dic[i] += 1
                answer += 1
            else:
                continue

    return answer