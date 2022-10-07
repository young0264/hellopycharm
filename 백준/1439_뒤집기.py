#0혹은 1 연속된숫자
import sys
input = sys.stdin.readline
arr = list(input().rstrip())
a,b = 0,0
for i in range(len(arr)-1):
    if arr[i]!=arr[i+1] and arr[i]=='0':# 0 -> 1
        a+=1
    elif arr[i]!=arr[i+1] and arr[i]=='1':# 1 -> 0
        b+=1
print()
print(a,b)
print(max(a,b))

