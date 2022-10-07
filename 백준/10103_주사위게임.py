n = int(input())
C = 100
S = 100
for i in range(n):
    a , b = map(int,input().split())
    if a == b :
        continue
    elif a > b :
        S -= a
    else :
        C -= b

print(C)
print(S)
