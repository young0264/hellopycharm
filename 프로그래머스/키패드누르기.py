from collections import deque


def solution(numbers, hand):
    global L,R
    keypad = [[1,2,3],[4,5,6],[7,8,9],[-1,0,-1]]
    def in_range(x, y):
        return 0 <= x < 4 and 0 <= y < 3

    def findLocation(n):
        for i in range(4):
            for j in range(3):
                if keypad[i][j] == n:
                    return i,j
    def bfs(A, goal):
        x, y = A
        visited = [[0] * 3 for _ in range(4)]
        visited[x][y] = 1
        visited[3][0], visited[3][2] = 1, 1
        que = deque()
        que.append((x, y))

        while que:
            dx, dy = que.popleft()
            if keypad[dx][dy] == goal:
                # if A == L:
                #     L = (dx,dy)
                # else:
                #     R = (dx,dy)
                return visited[dx][dy]

            for i in range(4):
                nx, ny = dx + dxs[i], dy + dys[i]
                if in_range(nx, ny) and not visited[nx][ny]:
                    visited[nx][ny] = visited[dx][dy] + 1
                    que.append((nx, ny))

    answer = ''
    L, R = (3, 0), (3, 2)

    L_numbers, R_numbers = [1, 4, 7], [3, 6, 9]
    dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0]
    dic = {1:(0,0),2:(0,1),3:(0,2),4:(1,0), 5:(1,1),
           6:(1,2), 7:(2,0),8:(2,1),9:(2,2), 0:(3,1)}

    for i in numbers:
        if i in L_numbers:
            answer += 'L'
            L = dic[i]  #여기가 문젠데
        elif i in R_numbers:
            answer += 'R'
            R = dic[i]

        else:
            res1 = bfs(L, i)
            res2 = bfs(R, i)
            print("res1, res2 : ", res1,res2)
            if res1 < res2:
                answer += 'L'
                a,b = findLocation(i)
                L = a,b
            elif res1 > res2:
                answer += 'R'
                a,b = findLocation(i)
                R = a,b
            else: #같을때
                a,b = findLocation(i)
                if hand == "right":
                    answer += 'R'
                    R = a,b
                else:
                    answer += 'L'
                    L=a,b
        print(answer)
        print("L",L)
        print("R",R)
        print()
    return answer
print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))