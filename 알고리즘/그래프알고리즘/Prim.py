#function prim(graph)                          // 그래프와 시작점 정보가 주어집니다.
#    set Q = Queue()                           // 우선순위 큐를 만들어줍니다.
#
#    for each vertex in graph                  // 그래프에 있는 모든 노드들에 대해
#        set dist[v] = INF                     // 초기값을 전부 아주 큰 값으로 설정해주고
#        Q.push(v)                             // 우선순위큐에 각 노드를 넣어줍니다.
#    set source = |V|                          // 시작점을 임의로 마지막 노드로 설정합니다.
#    set dist[source] = 0                      // 시작점 대해서만 dist 값을 0으로 초기화해줍니다.
#    while Q is not empty                      // 우선순위 큐가 비어있지 않을 때까지 반복합니다.
#        set u = vertex in Q with min dist     // 우선순위 큐에서 dist값이 가장 작은 노드를 선택합니다.
#        Q.remove(u)                           // 우선순위 큐에서 해당 노드를 제거해줍니다.
#
#        for each neighbor v of u              // u번 노드와 연결된 노드들을 전부 살펴보면서
#            set alt = length(u, v)            // 간선 가중치를 살펴봅니다.
#            if alt < dist[v]                  // 기존 dist값보다 더 alt값이 작다면
#                set dist[v] = alt             // dist값을 갱신해줍니다.
#