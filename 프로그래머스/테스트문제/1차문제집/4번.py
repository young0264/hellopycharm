from collections import deque

#그리디래
def solution(beginning, target):
    r, c = len(beginning), len(beggining[0])

    def check(graph):  # graph가 target과 같은지 체크
        global r, c
        flag = 0
        for i in range(r):
            for j in range(c):
                if graph[i][j] != target[i][j]:
                    return False
        return True

    #parameter로 주어지는 row/col에 해당하는 graph의 값들을 초기화
    def change(row, col, graph):  # 0,1,graph, graph1열을 바꿔
        global r, c
        if row:  # 열을 0~c까지
            for j in range(c):
                if graph[row][j] == 1:
                    graph[row][j] = 0
                else: graph[row][j] = 1

        elif col:  # 행을 0~r까지
            for i in range(r):
                if graph[i][col] == 1:
                    graph[i][col] = 0
                else: graph[i][col] = 1
        return graph

    def bfs(graph):
        global r,c
        for i in range(r):
            for j in range(c):



    answer = 0

    return answer
