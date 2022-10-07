dic = {}
for i in range(8):
    x = int(input())
    dic[i] = x
answer = 0
arr = list(sorted(dic,key = lambda x : -dic[x]))
arr = sorted(arr[:5])
for i in arr:
    answer += dic[i]
arr = list(map(lambda x:x+1,arr))
print(answer)
print(*arr)