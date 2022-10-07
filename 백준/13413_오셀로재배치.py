import sys
def input():
    return sys.stdin.readline().rstrip()
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(input())
    b = list(input())
    acnt = 0
    bcnt = 0
    answer = 0
    for i in range(n):
        if a[i] == 'B':
            acnt += 1
        if b[i] == 'B':
            bcnt += 1
    for i in range(n):
        if a[i] != b[i]:
            if acnt == bcnt :
                answer += 1/2
            elif acnt > bcnt :
                acnt -= 1
                answer += 1
            elif acnt < bcnt:
                bcnt -= 1
                answer += 1
    print(int(answer))

