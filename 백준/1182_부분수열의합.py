#조합을 dfs로 탐색해 뽑고 1~n(배열의길이만큼 뽑는 dfs를 거친다)
#3,4줄 둘다 Map으로 받으면 개인 정수인N은출력되는데 리스트 안한 arr은 안되는건 어케??
import sys
input = sys.stdin.readline
N,S = map(int,input().split())
arr=list(map(int,input().split()))
cnt = 0
def dfs(start, box):
    if len(box)==k :    #k가 배열길이만큼 돌꺼야
        result.append(box)
        return####
    for i in range(start,N):
        dfs(i+1,box + [arr[i]])
###result에는 arr의 요소들이 들어가야 하는건데
result=[]
for i in range(1,N+1):
    k=i
    dfs(0,[])
for i in result:
    if sum(i) == S:
        cnt+=1
print(cnt)

