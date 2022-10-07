import sys
input = sys.stdin.readline
n , k = map(int,input().split())
numbers = [i for i in range(1,4)]
res = []

def dfs(box):
    if sum(box) == n:    ##stop
        res.append(box)
        return
    if len(box) > n:       ##중복으로 들어가기 때문에 정수의값(1만넣었을때의 길이)
        return             ##을 초과하는 경우에 return
    for i in numbers:      ##재귀로 파고들기
        dfs(box+[i])
dfs([])
if len(res)<k:    #k번째 올만큼의 길이가 되지 않는경우
    print(-1)
    exit(0)
print('+'.join(map(str,res[k-1])))#map 을사용해 str형으로 바꿔준후 +간격으로 출력
