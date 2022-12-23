from itertools import product

def solution(k):
    arr = [6,2,5,5,4,5,6,3,7,6]
    nrr = [i for i in range(10)]
    answer = 0
    num = k//min(arr) +1

    for i in range(1,num):
        for permu in product(nrr,repeat = i):

            res = 0
            for j in permu:
                res += arr[j]
            if res == k :
                if len(permu)>1 and permu[0] == 0:
                    continue
                answer += 1
                # print(permu,num)
    return answer