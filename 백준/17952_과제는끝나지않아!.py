import sys
input = sys.stdin.readline
n = int(input())
stack = []
now = -1
score = 0
for _ in range(n):
    num = list(map(int,input().split()))
    if len(stack)>0 and num[0] == 0:
        stack[-1][1] -=1
    elif num[0]==1:   #arr[0]이 1일떄
        stack.append([num[1],num[2]-1])
    if len(stack)>0 and stack[-1][1] == 0:
        score += stack[-1][0]
        stack.pop()
print(score)



