#밑으로 가는 각 행을 조사하는 함수(반복문)하고
#그 매 반복문(매행)마다 모든 열을 조사하는 반복문.
# ex)1행에서 1열이 통과해야 2행3행.. 만약 False이면, 2열체크하게끔

n = int(input())
arr = [0]*n
cnt = 0
def is_promising_col(x) :#행값x   #행x에 대해 모든열을 조사하는거#한정함수
    for i in range(x):
        if abs(x-i) == abs(arr[x]-arr[i]) or arr[x]==arr[i] : #같은열, 대각선
            return False
    return True

# 재귀적으로 깊이&백탐색
def dfs(row):
    global cnt
    if row == n :
        cnt += 1
    else:
        for i in range(n):#n행의 반복으로
            arr[row] = i #row행의 i열, True가 되어야 i가 열값이 될 수 있겠지
            if is_promising_col(row) :
                dfs(row+1)
dfs(0)
print(cnt)


#a = (0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596)
#print(a[int(input())])