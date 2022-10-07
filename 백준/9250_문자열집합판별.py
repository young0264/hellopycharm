import sys
input= sys.stdin.readline
n1 = int(input())
zip = []
for i in range(n1):
    zip.append(input())
arr = []
n2 = int(input())
for i in range(n2):
    arr.append(input())

for i in range(len(arr)):
    flag = 0
    for j in zip:
        le = len(arr[i])-len(j)
        for t in range(le+1):
            if j == arr[i][t:t+le:1]:
                flag = 1
                print('YES')
                break
    if flag==0:
        print('NO')







