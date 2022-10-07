import sys
sys.setrecursionlimit(10**6)

n = int(input())
graph = [[] for _ in range(n+1)]    #깊은복사
for _ in range(n):
    arr = list(map(int,input().split()))
    for i in range(1,len(arr)-2,2) :
        graph[arr[0]].append((arr[i],arr[i+1]))
#visit = [0]*(n+1)
#print(graph)
#answer = 0

def dfs(start):
    visit = [0] * (n + 1)
    stack = [start]
    visit[start] = 1

    while stack:
        next = stack.pop()
        for node in graph[next]:
            if visit[node[0]] == False:
                stack.append(node[0])
                visit[node[0]] = visit[next] + node[1]  #(visit간선누적으로 true처리,),간선의길이
    return visit
print(dfs(2))
# dfs(n): n으로 시작하여 각 노드를 갈때의 간선의 길이의 합을 visitd의 각인덱2에 담음
res = dfs(1)
result = dfs(res.index(max(res)))
print(max(result)-1)    #방문처리를 위해 사용했던 1이 누적되어 더해지는거라 -1









################## left,right
#def dfs(start,d):
#    global answer
#    left , right = 0,0
#    for a,b in graph[start]:
#        x=0
#        if not visit[a]:
#            visit[a] = True
#            x = dfs(a,b)
#        if left <= right:
#            left = max(left, x)
#        else:
#            right = max(right, x)
#    answer = max(left+right,answer)
#    return max(left+d , right+d)
#visit[1]=True
#dfs(1,0)
#print(answer)