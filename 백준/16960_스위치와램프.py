import sys
def input():
    return sys.stdin.readline().rstrip()
n,m = map(int,input().split())

arr = []
dic = dict()

for i in range(n):
    lamp = list(map(int,input().split()))
    arr.append(lamp)
    for j in lamp[1:]:
        if (j) not in dic :
            dic[j] = 1
        else:
            dic[j] += 1
for i in arr:
    flag = 0
    for j in i[1:]:
        if dic[j]==1:
            flag = 1
            break

    if not flag :
        print(1)
        exit(0)
print(0)