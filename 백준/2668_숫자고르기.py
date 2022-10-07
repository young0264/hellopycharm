n = int(input())
arr = [0] + []
for _ in range(n):
    arr.append(int(input()))
ans_arr = []


def in_range(x):
    return 0 <= x < n


def dfs(idx):
    global start
    visited[idx] = 1
    nx = arr[idx]
    if not visited[nx]:
        visited[nx] = 1
        dfs(nx)
    elif nx == start:
        ans_arr.append(nx)

for i in range(1, len(arr)):
    visited = [0] * (n + 1)
    start = i
    dfs(i)
ans_arr.sort()
print(len(ans_arr))
for i in ans_arr:
    print(i)
