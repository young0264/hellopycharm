#인접노드를 계속 파고드는게 dfs

#되돌아가야하니까 방문처리를 해야해.
def dfs(node):#append배열만들기
    visit[node] = True
    for next in graph[node]:
        if not visit[next]:
            dfs(next)


def dfs(node):  #일단 node가 시작값
    graph=[]    #입력
    stack=[]  #완성본. 방문완료자들 넣는 스택
    stack[node] = True
    if node not in stack:   #방문처리를 한거면 빠져나가
        stack.append(node)
        for i in graph[node]:
            dfs(i)

def dfs(node):
    visited=[]
    graph[node]=True
    if not visited[node]:
        visited.append(node)
        for i in graph[node]:
            dfs(i)

def dfs(node):
    visited=[]
    graph[node]=True
    visited.append(node)
    for i in graph[node]:
        if not visited[i] : #방문처리를 한거면 빠져나가.끝
            dfs(i)

def dfs(node):
    visited=[]
    graph[node]=True
    visited.append(node)
    for i in graph[node]:
        if not visited[i] :
            dfs(i)



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


#append는 그 자체(배열이면배열 통으로)넣고
#extend는 그 원소들을 넣어줌.

if __name__ == "__main__":
    graph = {
        'A': ['B'],
        'B': ['A', 'C', 'H'],
        'C': ['B', 'D'],
        'D': ['C', 'E', 'G'],
        'E': ['D', 'F'],
        'F': ['E'],
        'G': ['D'],
        'H': ['B', 'I', 'J', 'M'],
        'I': ['H'],
        'J': ['H', 'K'],
        'K': ['J', 'L'],
        'L': ['K'],
        'M': ['H']
    }

    print(dfs(graph, 'A'))