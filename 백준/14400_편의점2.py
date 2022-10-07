import sys
def input():
    return sys.stdin.readline().rstrip()
n = int(input())
arrx = []
arry = []
for i in range(n):
    x,y = map(int,input().split())
    arrx.append(x)
    arry.append(y)
arrx.sort()
arry.sort()
sx = arrx[n//2]
sy = arry[n//2]
answer = 0
for i in range(n):
    answer += abs(arrx[i]-sx)
    answer += abs(arry[i]-sy)
print(answer)
