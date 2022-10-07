import sys
def input():
    return sys.stdin.readline().rstrip()
n,m = map(int,input().split())

def find2(x):
    cnt = 0
    while x:
        x = x//2
        cnt+=x
    return cnt

def find5(x):
    cnt = 0
    while x:
        x = x//5
        cnt+=x
    return cnt
answer = min(find2(n)-find2(n-m)-find2(m),find5(n)-find5(n-m)-find5(m))
print(answer)