n = int(input())
dp = [[[-1, -1]]*n for _ in range(n)]
# dp = [[[-1, -1] for _ in range(n)] for _ in range(n)]

graph=[]

for i in range(n):
    graph.append(list(map(int,input().split())))

dp[0][0][0] = graph[0][0]
dp[0][0][1] = graph[0][0]

print(dp[0][0][0])

for i in dp:
    print(i)

