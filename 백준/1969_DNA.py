n,m = map(int,input().split())

graph = [list(input()) for _ in range(n)]
set_lang = []
dic = dict()

for i in graph:
    set_lang += i
lang = sorted(list(set(set_lang)))

ans = ''
ans_value = 0
for j in range(m):
    for i in lang:dic[i] = 0
    for i in range(n):
        dic[graph[i][j]] += 1
    arr = [] #value

    for i in dic:
        arr.append(dic[i])
    max_value = max(arr)
    for i in dic:
        if max_value == dic[i]:
            ans += i
            break

for j in range(m):
    for i in range(n):
        if graph[i][j] != ans[j]:
            ans_value +=1

print(ans)
print(ans_value)




