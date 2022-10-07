#시계방향 90도 돌리기
from collections import deque

def rotate(key,n):    #정사각
    new_key = [[0]*n for _ in range(n)]
    for i in range(n):
        a,b = key[0][i], key[-1][i]
        c,d = key[i][0], key[i][-1]
        new_key[i][-1] = a
        new_key[i][0] = b
        new_key[0][-i-1] = c
        new_key[-1][-i-1] = d
    return new_key

def bfs(key,lock):



def solution(key, lock):
    answer = True
    n = len(key)
    m = len(lock)
    lock_arr = []
    #3배 좌표에 중앙만 값 초기화
    new_key = [[0]*3*n for _ in range(3*n)]
    for i in range(n,3*n-3):
        for j in range(n,3*n-n):
            new_key[i][j] = key[i-n][j-n]
    for i in range(m):
        for j in range(m):
            if lock[i][j] == '1':
                lock_arr.append((i,j))

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
n = 3
for i in rotate(key,n):
    print(*i)





    return answer