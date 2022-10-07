import sys
def input():
    return sys.stdin.readline().rstrip()
n,m = map(int,input().split())
arr = []
answer = 0
for i in range(n):
    a = input()
    arr.append(a)
for i in range(m):
    a = input()
    if a in arr:
        answer += 1
print(answer)
