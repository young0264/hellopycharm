n , m = map(int,input().split())
board = [list(map(int, input())) for _ in range(n)]

for i in range(1, n):
    for j in range(1, m):
        if board[i][j] == 1:
            board[i][j] = (min(board[i-1][j], board[i][j-1], board[i-1][j-1])+1)
re_value = 0
for i in range(n):
    re_value = max(max(board[i]),re_value)

print(re_value**2)