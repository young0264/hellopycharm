n = int(input())
visited = [[0]*(201) for _ in range(201)]

for idx in range(1,n+1):
    x1, y1, x2, y2 = list(map(int, input().split()))
    x1, y1, x2, y2 = x1+100, y1+100, x2+100, y2+100
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            if idx%2:
                visited[i][j] = -1
            elif not idx%2:
                visited[i][j] = 1
answer = 0
for i in range(201):
    for j in range(201):
        if visited[i][j] == 1:
            answer += 1
print(answer)

for i in visited:
    print(*i)