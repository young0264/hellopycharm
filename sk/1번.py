
def solution(p):
    answer = [0] * len(p)
    pre = []
    arr=[]

    for i in p :
        arr.append(i)
    pre.append(p)

    for i in range(len(arr)):
        pos = i  # min idx위치 저장
        for j in range(i , len(arr)):
            if arr[pos] > arr[j]:
                pos = j

        tmp = arr[pos]
        arr[pos] = arr[i]
        arr[i] = tmp

        pre.append(arr[:])
        #print("pre : ", pre)

        #print("answer :",answer)

    for j in range(len(pre[0])):
        for i in range(len(pre)-1):
            if pre[i][j] == pre[i+1][j]:
                continue
            else:
                answer[j]+=1

    return answer

arr = list(map(int, input().split()))
print(solution(arr))
