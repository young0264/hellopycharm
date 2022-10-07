n , m , k = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
k = k-1
#해당 행의 열에 블럭유무 확인
def check_block(row,col_s,col_e):
    return all ([
        not graph[row][col] for col in range(col_s,col_e+1)
    ])

#다음위치에 블럭이 존재하면 최종적으로 도달하게 될 위치는 현위치
def get_target_row():
    for row in range(n-1):
        if not check_block(row+1, k , k+m-1):#다음행의 열이False이면
            return row#현재열
    return n-1

stop_row = get_target_row()
graph[stop_row][k:k+m] = [1]*(m)
for i in graph:
    print(*i)

#멈추게 될 위치 변수에 초기화
#최종위치에 블럭표시