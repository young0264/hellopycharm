N, L = map(int,input().split())
arr = list(sorted(map(int,input().split())))
visited = [0]*1001
answer = 0
# for i in arr:
#     visited[i] = 1

for i in arr:
    if not visited[i]:
        length =int( i-0.5+L)
        if length > 1000:
            length = 1000
        for j in range(i,length+1):
            visited[j] = 1
        answer += 1

print(visited)
print(answer)
