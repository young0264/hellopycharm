def solution(queries):
    answer = []
    for query in queries:
        length = len(query)//2
        result = 0
        print("query : ", query)
        for i in range(length):
            res = abs(query[i] - query[-i-1])
            result += res
        print("result : ", result)
        print()
        if result%2 :
            answer.append(1)
        else:
            answer.append(0)

    print(answer)
    return answer
#그리디가 아니라 브루트포스인가.
# 1<=queries<=100
# 2<=초기배열길이<=5
# 0<=초기배열원소<=9
# 초기배열은 팰린드롬이 아니다.
# solution([[2,0],[3,1]])
# solution([[1,4,3], [1,2,2],[1,2,3]])
solution([[1,3,2,3,3]])