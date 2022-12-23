# 몬스터수, 초기체력
answer = 0
n, k = map(int, input().split())
A = list(map(int, input().split()))
P = list(map(int, input().split()))
dic1 = [[] for _ in range(max(A) + 1)]
for i in range(n):
    dic1[A[i]].append(P[i])
dic2 = [[] for _ in range(max(A) + 1)]

cnt = 0
for i in range(len(dic1)):
    for j in dic1[i]:  # i=1, j = 10,10,10,...
        k -= (i+cnt)
        cnt += i
        if k < 0:
            print(answer)
            exit(0)
        else:
            answer += j
print(answer)
