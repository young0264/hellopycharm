n = int(input())
flag = 1
for i in range(n):
    a,b = map(int,input().split())
    if a== flag:
        flag = b
    elif b==flag:
        flag = a

print(flag)