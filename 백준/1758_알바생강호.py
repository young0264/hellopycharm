#주려는돈이 높은놈부터 위로 배치하면 되지 않나
#332-> 3-1+1.3-2+1.2-3+1 => 3,2,0
import sys
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)
res = 0
for i in range(n):
    if arr[i]-i>0:
        res += arr[i]-i
print(res)