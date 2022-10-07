#2차원 좌표/ y축기준 잡아서 트리먼저 만들어야함

def solution(nodeinfo):
    answer = [[]]
    maxr,maxc = 0,0
    for c,r in nodeinfo:
        maxr = max(maxr,r)
        maxc = max(maxc,c)
    print(maxr,maxc)
    graph = [[0]*maxc for _ in range(maxr)]
    for c,r in nodeinfo:
        graph[r-1][c-1] = 1
    for i in graph:
        print(*i)
        # def preorder(root):
    #     answer.append(root)





    return answer


solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]])