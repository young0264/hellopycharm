def solution(info, edges):
    global answer

    def dfs(dx, sheep, wolf,box):
        global answer
        print("dx,sheep,wolf", dx, sheep, wolf)
        if info[dx] == 0:
            sheep += 1
            answer = max(answer,sheep)
        else:
            wolf += 1
        if wolf >= sheep :
            return
        box.extend(edges_arr[dx])
        #############
        for nx in box:
            arr = []
            for nnx in box:
                if nnx != nx:
                    arr.append(nnx)
            dfs(nx,sheep, wolf, arr)

    answer = 0
    # visited = [0] * len(info)
    edges_arr = [[] for _ in range(len(info))]

    for i in range(len(edges)):
        parent, child = edges[i][0], edges[i][1]
        edges_arr[parent].append(child)

    dfs(0, 0, 0,[])
    return answer


info = [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1]
edges = [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]
print(solution(info, edges))
