def solution(lotteries):
    answer = 0
    length = len(lotteries)
    arr = []
    for i in range(length):
        a,b,c = lotteries[i]
        percent = a/(b+1)
        if percent >= 1:
            percent = 1
        arr.append([percent,c,i])
    res = sorted(arr, key=lambda x:(-x[0],-x[1]))
    # print(dic)
    # print(res[0][1])
    answer = res[0][2]+1
    return answer
# print(solution([[100, 100, 500], [1000,1000,100]]))
# print(solution([[10, 19, 800], [20,39,200],[100, 199,500]]))
print(solution([[1000,1000,10],[1000,1000,20]]))