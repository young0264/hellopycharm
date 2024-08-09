import sys
input = sys.stdin.readline

n,m = map(int,input().split())
answer = 0
arr = []
brr = []
dic = dict()
for _ in range(n):
    s = input().rstrip()
    arr.append(s)
    if s[0] in dic:
        dic[s[0]].append(s)
    else:
        dic[s[0]] = [s]
for _ in range(m):
    s = input().rstrip()
    brr.append(s)

brr.sort()
print(dic)
for i in range(m):
    if brr[i][0] in dic:
        for res in dic[brr[i][0]]:
            print(res,brr[i])
            if res.startswith(brr[i]):
                answer += 1
                break

print(answer)