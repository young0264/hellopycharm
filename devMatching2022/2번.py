from collections import deque

def solution(maps):
    graph = []
    for map in maps:
        graph.append(list(map))

    r,c = len(graph), len(graph[0])
    visited = [[0]*c for _ in range(r)]
    dxs,dys = [0,0,1,-1],[1,-1,0,0]
    answer = 0

    def in_range(x,y):
        return 0<=x<r and 0<=y<c

    def bfs(x,y):
        que = deque()
        que.append((x,y))
        visited[x][y] = 1
        dic = dict()
        alphabet_pos = dict()
        dic[graph[x][y]] = dic.get(graph[x][y],0) + 1
        alphabet_pos[graph[x][y]] = [(x,y)]
        while que:
            dx,dy = que.popleft()
            for i in range(4):
                nx,ny = dx+dxs[i],dy+dys[i]
                if in_range(nx,ny) and graph[nx][ny] != '.' and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    dic[graph[nx][ny]] = dic.get(graph[nx][ny],0) + 1
                    if graph[nx][ny] not in alphabet_pos:
                        alphabet_pos[graph[nx][ny]] = [(nx,ny)]
                    else:
                        alphabet_pos[graph[nx][ny]].append((nx,ny))

                    que.append((nx,ny))

        max_key = ''
        max_value = 0
        for i in dic:
            if dic[i] > max_value:
                max_key = i
                max_value = dic[i]
        arr = []
        for i in dic:
            if dic[i] == max_value:
                arr.append(i)
        arr.sort()
        last_alphabet = arr[-1]
        s = set(arr)
        # print("last_alphabet",last_alphabet)
        # print(max_key,max_value)
        # print("alphabet_pos",alphabet_pos)
        for i in alphabet_pos:
            # print(alphabet_pos[i])
            if i not in s:
                for nnx,nny in alphabet_pos[i]:
                    graph[nnx][nny] = last_alphabet

    for i in range(r):
        for j in range(c):
            if not visited[i][j] and graph[i][j] != '.':
                bfs(i,j)
    ans_dic = dict()
    for i in range(r):
        for j in range(c):
            if graph[i][j] != '.':
                ans_dic[graph[i][j]] = ans_dic.get(graph[i][j],0)+1

    answer = (max(ans_dic.values()))
    return answer