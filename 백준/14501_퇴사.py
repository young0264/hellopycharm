n = int(input())
T = []
P = []
D = [0]*(n+1)

for _ in range(n):
    a,b = map(int,input().split())
    T.append(a)
    P.append(b)

for i in range(n):
    for j in range(T[i]+i,n+1):
        if D[j] < D[i]+P[i]:
            D[j] = D[i] + P[i]


print(max(D))