m,n,v = map(int,input().split())
graph = [[] for _ in range(m + 1)]
visit = [0] * (m + 1)
visitStack = []
for i in range(n):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(node):
    visit[node] = True
    visitStack.append(node)
    for next_node in sorted(graph[node]):
        if not visit[next_node]:
            dfs(next_node)
dfs(v)
print(visitStack)


#-----------------

def dfs(graph,start_node):
    visited =[]
    need_visit = []         #시작노드를 담는 리스트
    need_visit.append(start_node)#시작지점 넣어주고

    while need_visit :      #시작노드가 담겨져 있는 배열
        node = need_visit.pop() #시작노드를 빼낸거를 node에 담음
        if node not in visited:  #중복되면 visited배열에 담지말고.
            visited.append(node) #스택에서 데이터를 하나 꺼내서 방문했다고 적어.나중에 출력할꺼야
            for i in graph[node]:
                need_visit.append(i)
            #need_visit.extend(graph[node])
    return visited


def recursive_dfs(v,discovered=[]):
    discovered.append(v)
    for w in graph[v]:
        if w not in discovered:
            discovered=recursive_dfs(w, discovered)
    return discovered

#graph=[[],[1,2],[3,4],[5,6]]
graph={1:[2,3,4],2:[5],3:[5],4:[],5:[6,7],6:[],7:[3]}
discovered=[]

print(recursive_dfs(1,discovered=[]))