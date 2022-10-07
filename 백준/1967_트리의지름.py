#그냥 누적합개념이 아닌걸 설명을 할 줄 알아야해
import sys
sys.setrecursionlimit(10**6)
n = int(input())
arr = [[] for _ in range(n+1)]

for i in range(n-1):
    a,b,c = map(int,input().split())
    #arr[a] = b,c
    arr[a].append((b,c))
answer = 0 #어떤노드의 지름 최댓값
gwa = []
def dfs(start,d,box) : #x==1 부터 시작
    #global answer
    box += d
    #left , right = 0,0
    for a,b in arr[start] :    # 자식노드
        dfs(a,b,box)
        #if left <= right :
        #    left = max(x,left)
        #else :
        #    right = max(x,right)
        #answer = max(right+left, answer)
    gwa.append(box)
    print(box)
    return box #max(d+left, d+right)
#dfs(1,0,0)
print(dfs(3,0,0))
print(gwa)
