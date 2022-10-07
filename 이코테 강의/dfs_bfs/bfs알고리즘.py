#앞서 주어진 인접노드들 먼저 우선순으로 하여 탑색하는거
from collections import deque
# bfs : 너비우선탐색. 현재 정점에 연결된 가까운 점들부터 탐색
#     : Queue
def bfs(start) :
    need_visit = deque()
    visited = []
    graph = []
    need_visit.append(start)
    while need_visit:
        node = need_visit.popleft()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    return visited


def bfs(start):
    need_visit = deque()
    visited = []
    graph = []
    need_visit.append(start)
    while need_visit:               #1번질문
        node = need_visit.popleft() #node값이 n.v.의 pop값이란걸 명시만 하는건가
                                    #pop을하고 & 그리고 그값이 node에 들어간단건가
        if not visited:             #pop이 된거면 if not need_visited할만함
            visited.append(node)
            need_visit.extend(graph[node])
    return visited


from collections import deque
def bfs(graph, start_node):
    visited = list() #출력용
    need_visit=deque() #큐용
    need_visit.append(start_node)   #바로 visited에 넣지않고
    while need_visit:               #need_visit에 넣음으로써 반복문에서 판별하도록
        node = need_visit.popleft() #편하게 popleft에 대한 변수 만들어주고
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])#인접합녀석들을 need_visit에넣어
                         #need_visit이 안비어있으면 여기서 다시 while로 돌아가지
    return visited  #?

#----------------
from collections import deque       #여기서 그래프는 2차원리스트
def bfs(graph,start,visited):
    queue = deque()
    queue.append(start)
    visited[start] = True #방문처리
    while queue :
        v = queue.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if not graph[v]:
                queue.append(i)
                visited[i] = True
visited = [False]*9

bfs(graph,1,visited)