#가장 가까운 두 사람의 거리를 최대
import sys
n = int(input())
s = list(input())
answer = 0
def check_place(idx):
    new_s = s[::]
    visited = [0]*n
    new_s[idx] = '1'
    res = sys.maxsize
    # print(new_s)
    for i in range(n):
        if new_s[i] == '1':
            visited[i] = i
        else:
            if i == 0:
                visited[i] = 0
            else:
                visited[i] = visited[i-1]
    for i in range(1, n):
        if visited[i] != visited[i-1]:
            result = visited[i] - visited[i-1]
            res = min(res, result)
    return res

for i in range(n):
    if i==0 and s[i+1] == '0' and s[i]=='0':
        res = check_place(i)
        answer = max(answer, res)
    elif i == n-1 and s[i-1]=='0' and s[i]=='0':
        res = check_place(i)
        answer = max(answer, res)
    elif s[i-1]=='0' and s[i+1]=='0' and s[i] != '1':
        res = check_place(i)
        answer = max(answer,res)
print(answer)