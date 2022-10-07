import sys
from collections import defaultdict
from bisect import bisect_left
def input():
    return sys.stdin.readline().rstrip()
n,m = map(int,input().split())
dic = defaultdict(list)
B = []
for i in range(n):
    num = int(input())
    B.append(num)
B.sort()
for i in range(n):
    if B[i] not in dic:
        dic[B[i]].append(i)
    else:
        dic[B[i]].append(i)
#print(dic)
#print("dic : ", dic)
#print("B : ", B)
for i in range(m):
    pos = int(input())
    x = bisect_left(B,pos)
    #print("x = ", x)

    if pos > B[-1]:
        print(-1)
        continue
    if pos < B[0]:
        print(-1)
        continue
    if B[x] == pos:
        print(dic[pos][0])
    else:
        print(-1)

