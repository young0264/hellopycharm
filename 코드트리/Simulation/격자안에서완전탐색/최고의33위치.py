n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
res = []
for i in range(n - 2):
    for j in range(n - 2):
        cnt = 0
        for k in range(i, i + 3):
            for t in range(j, j + 3):
                if graph[k][t] == 1:
                    cnt += 1
        res.append(cnt)
print(max(res))